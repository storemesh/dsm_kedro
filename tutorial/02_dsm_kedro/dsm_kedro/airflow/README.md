# Airflow Docker 

to custom official Airflow docker compose file to our kedro version, needed to edit docker compose a little bit as follow
```yml
x-airflow-common:
  &airflow-common

  ...

  build:
    # build at root of project
    context: ..
    dockerfile: airflow/Dockerfile
  env_file:
    - ../.env
    
  ...

  volumes:
    ...
    - ../etl-pipeline/airflow_dags:/opt/airflow/dags    
    - ../etl-pipeline:/etl-pipeline

```
