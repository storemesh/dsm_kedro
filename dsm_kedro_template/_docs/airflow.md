# Run pipeline in Airflow

1. generate airflow dags 
```sh
# at etl-pipeline/
kedro airflow create --target-dir=airflow_dags/  --pipeline=<your_pipeline_name>
```
**Note:** you can use '__default__' as <your_pipeline_name>

2. edit schedule and add other config in `airflow_dags/<your_pipeline_name>` as follow
    - specific runner to generate run logs
    ```python
    ...    
    import sys
    import os
    sys.path.append(os.getcwd())

    from airflow.operators.python_operator import PythonOperator
    from kedro.framework.startup import bootstrap_project
    from src.dsm_kedro_plugin.custom_runner.dsm_runner import WriteFunctionLogRunner
    from src.dsm_kedro_plugin.custom_runner.utils.logs_generator import gen_log_start, gen_log_finish
    ...

    class KedroOperator(BaseOperator):
        ...
        # replace execute method with this
        def execute(self, context):
            bootstrap_project(project_path)
            with KedroSession.create(self.project_path, env=self.env) as session:
                session.run(
                    self.pipeline_name,
                    node_names=[self.node_name],
                    runner=WriteFunctionLogRunner(),
                )
    ```
    - change schedule to your desire crons expression
    ```python
        with DAG(
            ...
            schedule_interval="0 0 * * *",  # see more https://airflow.apache.org/docs/stable/scheduler, https://crontab.guru/
            ...
        ) as dag:
    ```
    - add `start_node` and `end_node` to generate log
    ```python
    ...
    tasks= {}

    tasks['start_node'] = PythonOperator(
        task_id='start_node', 
        python_callable=gen_log_start, 
        op_kwargs={'pipeline_name': pipeline_name},
    )

    tasks['end_node'] = PythonOperator(
        task_id='end_node', 
        python_callable=gen_log_finish, 
        op_kwargs={'pipeline_name': pipeline_name},
    )
    ...

    tasks["start_node"] >> [tasks[<YOUR FIRST RUN TASK NAME>], tasks[<YOUR FIRST RUN TASK NAME>]]

    ...

    tasks[<YOUR INTEGRATION TASK NAME>] >> tasks["end_node"]
    ```

3. create .env file
```
PROJECT_NAME=<YOUR_PROJECT_NAME>
```
4. run Airflow with docker compose
```
cd airflow
docker compose up --build
```

5. go to localhost:8084 and login with default username and password

## FAQ
if you have problem with folder permission, use this following command
```sh
sudo chgrp -R root * && sudo chmod -R 770 *
```