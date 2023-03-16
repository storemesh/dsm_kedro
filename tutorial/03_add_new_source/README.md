# Kedro Add New Source Example

## Prerequisite
- docker compose v2
- python >= 3.8
- miniconda

# 1. Deploy Database
```
cd data_source
docker compose up -d
```

# 2. Run Kedro
## Prepare Environment and Setting
1. go to kedro root project
```sh
cd .. # dsm_kedro/etl-pipeline
```
2. create conda env and activate

```sh
conda create -n kedro-<YOUR_PROJECT_NAME> python=3.8  
# press y
source activate kedro-<YOUR_PROJECT_NAME>
```

3. install require package
```sh
# at etl-pipeline/
pip install -r src/requirements.txt
```

4. (optional) create new ipython kernel 

```sh
python -m ipykernel install --user --name kedro-env --display-name "Python (kedro-env)"
```

5. create credentials file for using dsm library
```yml
# in conf/local/credentials.yml
dsmlibrary:
    token: "< YOUR JWT TOKEN >"
```
6. clone submodule project
```
cd etl-pipeline/src/dsm_kedro_plugin
git submodule update --init --recursive
```

7. 

## Run Pipeline
### Run Integration (have only system1)
1. run system1 staging
```
kedro run --pipeline=system1_exporter
```
2. run integration exporter
```
kedro run --pipeline=dim_exporter
```

### Add System2 source code
3. add database in data discovery backend
4. generate sql datanode and landing
5. run query_landing pipeline
6. create pipeline
7. 

