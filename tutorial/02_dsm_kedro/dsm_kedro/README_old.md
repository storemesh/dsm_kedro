# Kedro Template
## Install
### Clone Source Code Template
1. clone Kedro Template for dsm
```sh
git clone https://gitlab.com/storemesh/project-template/data-engineer/kedro-template/kedro-template.git
```

2. clone dsm-kedro-plugin
```sh
cd etl-pipeline/src/dsm-kedro-plugin
git submodule init
git submodule update
```

## Prepare Environment and Setting

1. create conda env and activate

```sh
conda create -n kedro-environment python=3.8  
# press y
source activate kedro-environment
```

2. install require package
```sh
# at kedro-template/etl-pipeline
pip install -r src/requirements.txt
```

3. create new ipython kernel

```sh
python -m ipykernel install --user --name kedro-env --display-name "Python (kedro-env)"
```

4. create credentials file for using dsm library
```yml
# in conf/local/credentials.yml
dsmlibrary:
    token: "< YOUR JWT TOKEN >"
```



# Development Step
## For Data Generator Role

1. copy source and integration config template (do only first time)
```sh
# in dsm-kedro-plugin
cp -R generate_datanode/config_template ../config
```

2. change sql_datanode, landing and integration config (desire table and destination folder id)
- (temporary): change `db_connection` and `db_schema` in `src/generate_datanode/config/config_database.py`
- change `source_table`, `sql_datanode_folder_id` and `landing_folder_id` in `src/generate_datanode/config/config_source_table.py`
- change `integration_folder_id` and `integration_table` in `src/generate_datanode/config/config_integration_table.py`


3. generate sql_datanode, landing and integration
```sh
cd src/generate_datanode
```
- generate sql_datanode (auto write SQLDataNode to data platform)
```sh
python 01_generate_sql_datanode.py
```
- generate landing catalogs, nodes and pipelines file
```sh
python 02_generate_landing.py
```
- generate integration catalogs
```sh
python 03_generate_integration.py
# set APPEND_MODE to True, if you want to write file in append mode and partition on date
```

4. run generate_change_landing pipeline 
```sh
cd ../.. 
# to base directory
```
- run query landing pipeline
```sh
kedro --pipeline=query_landing
```

## For Data Engineer Role

1. create your desire pipeline
```sh
kedro pipeline create <your_pipeline_name>
# for example : kedro pipeline create export_integration
```
2. create catalog file at `conf/base/catalogs/manual/<your_pipeline_name>.yml`  to define staging dataset. Use the following format
```yml
# conf/base/catalogs/manual/<your_pipeline_name>.yml
staging___<database_name>___<table_name>___<field_name>:
  type: custom_dataset.dsm_dataset.DsmDataNode
  folder_id: <folder_id>
  file_name: staging___<database_name>___<table_name>___<field_name>
  credentials: dsmlibrary
```

3. edit your pipeline.py at `src/etl_pipeline/pipelines/<your_pipeline_name>/pipeline.py` in this pattern
```python
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import my_task_staging_function, my_task_integration_function

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
      [
          # staging
          node(
              func=my_task_staging_function,
              inputs="<your input dataset name>",  
              outputs="<your output dataset name>",
              name="<your output dataset name>___node",
          ),

          # integration
          node(
              func=my_task_integration_function,
              inputs=["<your input dataset name1>", "<your input dataset name2>"],  
              outputs="<your output dataset name>",
              name="<your output dataset name>___node",
          ),
          ## see more example in : pipelines/generate_change_landing/pipeline.py
      ]
    )

```

4. edit your nodes.py at `src/etl_pipeline/pipelines/<your_pipeline_name>/nodes.py`
```python
import dask.dataframe as dd
from typing import List, Tuple

#### for staging
def my_task_staging_function(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]] :
    ddf, file_id = data
    
    # your source code here
    # Note: staging column name should be in this pattern
    #       pk, input, output

    lineage_id = [file_id]
    return (ddf, lineage_id)

#### for integration
def my_task_integration_function(
        data_column1 : Tuple[dd.DataFrame, int],
        data_column2 : Tuple[dd.DataFrame, int],
    ) -> Tuple[dd.DataFrame, List[int]] :
    ddf, file_id = data
    
    # your source code here

    lineage_id = [file_id]
    return (ddf, lineage_id)
```

5. add your pipeline to `src/etl_pipeline/pipeline_registry.py`
```python
# src/etl_pipeline/pipeline_registry.py
...
from etl_pipeline.pipelines.<your_pipeline_name> import pipeline as <your_alise>

def register_pipelines() -> Dict[str, Pipeline]:
    ...
    <your_pipeline_name> = <your_alise>.create_pipeline()

    return {
        ...
        "<your_pipeline_name>" : <your_pipeline_name>
    }
```

6. run your pipeline
```sh
kedro run --pipeline=<your_pipeline_name>
```

7. run your pipeline on specific node
```sh
kedro run --pipeline=<your_pipeline_name> --node=<your_node_name>
```
### Other Pipeline

- run all '__default' pipelines
```
kedro run
```
- run update latest landing table
```
kedro run --pipeline=update_latest_landing
```


# Run pipeline in Airflow
1. generate airflow dags 
```sh
# at etl-pipeline/
kedro airflow create --target-dir=airflow_dags/  --pipeline=<your_pipeline_name>
```
note: you can use '__default__' as <your_pipeline_name>
2. build kedro project to whl file for installing in Airflow
```sh
kedro package
```
3. run Airflow with docker compose
```
cd airflow
docker compose up
```
4. go to localhost:8084 and login with default username and password


## FAQ
if you have problem with folder permission, use this following command
```sh
sudo chgrp -R root * && sudo chmod -R 770 *
```

# Library Development
dsm library
```sh
cd <your_library_development_path>
pip install -e git+https://gitlab.com/public-project2/dsm-library.git@development#egg=dsmlibrary
```


kedro run --pipeline=Payment --node=integration___Payment___node  --runner=dsm_kedro_plugin.custom_runner.dsm_runner.DsmRunner

