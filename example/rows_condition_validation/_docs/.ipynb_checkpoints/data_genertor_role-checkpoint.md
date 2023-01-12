# For Data Generator Role
Data Generator Role is a role that have resiponsible to do the following process
1. create project template in Data Discovery from `project folder id`
2. (optional) create SQLDataNode and Landing Zone (if you have database as data source) 
    - Generate Data Catalog in Kedro (`conf/base/catalogs/generate/catalog_01_sql_datanode.yml` and `conf/base/catalogs/generate/catalog_02_landing.yml`)
    - Generate Pipeline in Kedro (`src/etl_pipeline/pipelines/query_landing`)
3. create Data Catalog for Integration Zone (`catalog_03_integration.yml`)
4. (optional) add query_landing to `src/etl_pipeline/pipeline_registry.py` (do this if you do the step 2)
5. (optional) generate Landing Data to Landing Zone (do this if you do the step 2, 4)


# Step

1. create project template in Data Discovery from `project folder id`

    1.1. copy source and integration config template (do only first time)
    ```sh
    cp -R src/dsm_kedro_plugin/generate_datanode/config_template src/config
    ```

    1.2. go to `src/config/project_setting.py` and put the following value
        - PROJECT_NAME: your project name (exactly the same value in Project Table of Data Discovery, use it for generate logs)
        - PROJECT_FOLDER_ID: your project folder id

    1.3. create project template in Data Discovery by running this script
    ```sh
    python src/dsm_kedro_plugin/create_project_template.py
    ```
    Check in your project folder Data Discovery, you will see the following folder 
        - SQLDataNode
        - Landing
        - Staging
        - Integration
        - Logs
    
2. (optional) create SQLDataNode and Landing Zone (if you have database as data source) 


    2.1. open `src/config/config_source_table.py` and `source_table` by adding database connection id (from Data Discovery) and source table name (same value in Data Discovery)

    2.2. go to generate folder
    ```sh
    cd src/generate_datanode
    ```

    2.3. generate sql_datanode (auto write SQLDataNode to data platform)
    ```sh
    python 01_generate_sql_datanode.py
    ```
    This will generate the following files
    - `conf/base/catalogs/generate/catalog_01_sql_datanode.yml`
    - sql datanode files in your `SQLDataNode` folder (in Data Discovery)

    2.4. generate landing catalogs, nodes and pipelines file
    ```sh
    python 02_generate_landing.py
    ```
    This will generate the following files
    - `conf/base/catalogs/generate/catalog_02_landing.yml`
    - `src/etl_pipeline/pipelines/query_landing/nodes.py`
    - `src/etl_pipeline/pipelines/query_landing/pipeline.py`

3. create Data Catalog for Integration Zone  

    run this command to generate integration catalogs
    ```sh
    python 03_generate_integration.py
    # set APPEND_MODE to True, if you want to write file in append mode and partition on query date
    ```
    This will generate the following files
    - `conf/base/catalogs/generate/catalog_03_integration.yml`

4. (optional) add query_landing to `src/etl_pipeline/pipeline_registry.py` (do this if you do the step 2)

    ```python
    # src/etl_pipeline/pipeline_registry.py
    ...
    from etl_pipeline.pipelines.query_landing import pipeline as ql

    def register_pipelines() -> Dict[str, Pipeline]:
        ...
        query_landing = ql.create_pipeline()

        return {
            ...
            "query_landing" : query_landing
        }
    ```


5. (optional) generate Landing Data to Landing Zone (do this if you do the step 2, 4)   

    4.1 to base directory of kedro
    ```sh
    cd ../.. 
    # kedro-template/etl-pipeline/
    ```
    4.2 To run landing in specific source, check `your_node_name` in `src/etl_pipeline/pipelines/query_landing/pipeline.py`, copy and run this command
    - run query landing pipeline
    ```sh
    kedro run --pipeline=query_landing --node=<your_node_name>
    ```

    **Note:** If you want to run all landing source, you can run without --node parameter
    - run query landing pipeline
    ```sh
    kedro run --pipeline=query_landing
```

