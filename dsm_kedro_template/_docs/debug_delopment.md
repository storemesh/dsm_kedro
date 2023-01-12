# Debug and Development

## Jupyter
You can check and load your data catalog in Jupyter by following step
- open jupyter
```sh
# dsm_kedro/etl-pipeline 
jupyter notebook
```
- add this code to first cell
```python
import sys
sys.path.append('YOUR_WORKING_DIRECTORY>/dsm_kedro/etl-pipeline')

%load_ext kedro.ipython
```

- see catalog list
```python
catalog.list()
```

- load data catalog 
```python
catalog.load("<DATA_CATALOG_NAME>")
```

You can see example kedro load for DsmDatanode in [example_kedro_load.ipynb](../etl-pipeline/notebooks/example_kedro_load.ipynb)

For more detail about jupyter and kedro, please visit https://kedro.readthedocs.io/en/stable/notebooks_and_ipython/kedro_and_notebooks.html

## Visualize Pipeline
- To visualize pipeline with kedro viz
    ```sh
    kedro viz
    ```

    for autoreload
    ```sh
    kedro viz --autoreload
    ```

    The pipeline visualization will ready on http://127.0.0.1:4141/. 

## Library Development
- dsm library

    - activate to your python environment 
    - run this command to install in development mode 
        ```sh
        cd <your_library_development_path>
        pip install -e git+https://gitlab.com/public-project2/dsm-library.git@development#egg=dsmlibrary
        ```

- dsm kedro plugin

    To add new feature, you can edit `etl-pipeline/src/dsm_kedro_plugin`, push to gitlab and make merge request to branch main
