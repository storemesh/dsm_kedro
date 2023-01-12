# Run pipeline in Airflow

1. generate airflow dags 
```sh
# at etl-pipeline/
kedro airflow create --target-dir=airflow_dags/  --pipeline=<your_pipeline_name>
```
**Note:** you can use '__default__' as <your_pipeline_name>

2. edit schedule and other config in `airflow_dags/<your_pipeline_name>` to your desired value

3. build kedro project to whl file for installing in Airflow
```sh
kedro package
```

4. run Airflow with docker compose
```
cd airflow
docker compose up
```

5. go to localhost:8084 and login with default username and password

## FAQ
if you have problem with folder permission, use this following command
```sh
sudo chgrp -R root * && sudo chmod -R 770 *
```