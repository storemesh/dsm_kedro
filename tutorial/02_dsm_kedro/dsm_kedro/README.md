# Kedro Template
## Install and Setup
### Clone Source Code Template
1. clone Kedro Template for dsm
```sh
git clone https://gitlab.com/storemesh/project-template/data-engineer/kedro-template/kedro-template.git
```

2. clone dsm_kedro_plugin
```sh
cd etl-pipeline/src/dsm_kedro_plugin
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
[see here](_docs/data_generator_role.md)

## For Data Engineer Role
[see here](_docs/data_engineer_role.md)

# Run Step
- To run all pipeline (__default__ pipeline)
```sh
kedro run
```

- To run specific pipeline (see pipeline name in `etl-pipeline/src/etl_pipeline/pipeline_registry.py`)
```sh
kedro run --pipeline=<pipeline_name>
```

# Visualize Pipeline
- To visualize pipeline with kedro viz
    ```sh
    kedro viz
    ```

    for autoreload
    ```sh
    kedro viz --autoreload
    ```

    The pipeline visualization will ready on http://127.0.0.1:4141/. 

# Run pipeline in Airflow
[see here](_docs/airflow.md)

# Library Development
- dsm library

    - activate to your python environment 
    - run this command to install in development mode 
        ```sh
        cd <your_library_development_path>
        pip install -e git+https://gitlab.com/public-project2/dsm-library.git@development#egg=dsmlibrary
        ```

- dsm kedro plugin

    To add new feature, you can edit `etl-pipeline/src/dsm_kedro_plugin`, push to gitlab and make merge request to branch main
