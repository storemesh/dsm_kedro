## For Data Engineer Role
Data Engineer Role is a role that have resiponsible to do the following process
1. create your pipeline in kedro
2. (optional) create catalog file
3. edit your pipeline.py 
4. edit your nodes.py
5. add your pipeline to `src/etl_pipeline/pipeline_registry.py`
6. run your pipeline

# Step
1. create your pipeline in kedro

    ```sh
    kedro pipeline create <your_pipeline_name>
    # for example : kedro pipeline create Export
    ```
    
2. (optional) create catalog file

    create catalog file at `conf/base/catalogs/manual/<your_pipeline_name>.yml`  to define some of the following list    
        - Landing catalog : create it if your pipeline data source input are not from database (from scraping, api, manual upload and etc.)   
        - Staging dataset : create it if you want to do hugh preprocess work   

    Manual Data Catalog format
    ```yml
    # conf/base/catalogs/manual/<your_pipeline_name>.yml

    # for Landing dataset
    landing___<your_desired_name>:
      type: dsm_kedro_plugin.custom_dataset.dsm_dataset.DsmDataNode
      folder_id: <landing_folder_id>
      file_name: landing___<your_desired_name>
      credentials: dsmlibrary

    # for Staging dataset
    staging___<database_name>___<table_name>:
      type: dsm_kedro_plugin.custom_dataset.dsm_dataset.DsmDataNode
      folder_id: <staging_folder_id>
      file_name: staging___<database_name>___<table_name>
      credentials: dsmlibrary
    ```
    **Note:** Data Engineer Role will not create Integration table directly. Contact Data Generator role to generate Integration Catalog (the name of Integration table need to be exactly same with Data Product)

3. edit your pipeline.py at `src/etl_pipeline/pipelines/<your_pipeline_name>/pipeline.py` in this pattern

    ```python
    from kedro.pipeline import Pipeline, node, pipeline
    from .nodes import <your_function01>, <your_function02>



    def create_pipeline(**kwargs) -> Pipeline:
        return pipeline(
          [
              # one input data
              node(
                  func=<your_function01>,
                  inputs="<your input dataset name>",  
                  outputs="<your output dataset name>",
                  name="<your output dataset name>___node",
              ),

              # several input data
              node(
                  func=<your_function02>,
                  inputs=dict(
                      data1: "<your input dataset name1>", 
                      data2: "<your input dataset name2>"
                  ),  
                  outputs="<your output dataset name>",
                  name="<your output dataset name>___node",
              ),
              ## see more example in : pipelines/query_landing/pipeline.py
          ]
        )

    ```

4. edit your nodes.py at `src/etl_pipeline/pipelines/<your_pipeline_name>/nodes.py`   
    ```python
    import dask.dataframe as dd
    from typing import List, Tuple

    #### for one input
    def <your_function01>(data: Tuple[dd.DataFrame, Dict]) -> Tuple[dd.DataFrame, List[Dict]] :
        ddf, meta = data    
        # your source code here

        lineage_list = [meta]
        return (ddf, lineage_list)

    #### for several input
    def <your_function02>(
            data1 : Tuple[dd.DataFrame, int],
            data2 : Tuple[dd.DataFrame, int],
        ) -> Tuple[dd.DataFrame, List[int]] :
        ddf1, meta1 = data1
        ddf2, meta2 = data2
        # your source code here

        lineage_list = [meta1, meta2]
        return (ddf, lineage_list)
    ```

5. add your pipeline to `src/etl_pipeline/pipeline_registry.py`    
    ```python
    # src/etl_pipeline/pipeline_registry.py
    ...
    from etl_pipeline.pipelines.<your_pipeline_name> import pipeline as <your_pipeline_name>_obj

    def register_pipelines() -> Dict[str, Pipeline]:
        ...
        <your_pipeline_name>_pipeline = <your_pipeline_name>_obj.create_pipeline()

        return {
            ...
            "<your_pipeline_name>" : <your_pipeline_name>_pipeline
        }
    ```

6. run your pipeline    
run your specific node in pipeline 
    ```sh
    kedro run --pipeline=<your_pipeline_name> --node=<your_node_name>
    ```

run with generate logs in Data Discovery
    ```sh
    kedro run --pipeline=Payment --node=integration___Payment___node  --runner=dsm_kedro_plugin.custom_runner.dsm_runner.DsmRunner
    ```

    **Other Run Command**   
    - run all pipeline   
    ```sh
    kedro run --pipeline=<your_pipeline_name>
    ```

    - run all '__default' pipelines  
    ```sh
    kedro run
    ```

    - run update latest landing table  
    ```sh
    kedro run --pipeline=query_landing
    ```