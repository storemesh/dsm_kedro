# Run pipeline in Airflow

## No Write Logs to logs pipeline
1. generate airflow dags 
```sh
# at etl-pipeline/
kedro airflow create --target-dir=airflow_dags/  --pipeline=<your_pipeline_name>
```
**Note:** you can use '__default__' as <your_pipeline_name>

2. go to airflow_dags/etl_pipeline.py, rename it to <your_pipeline_name>
3. replace top of file with this (don't forget to replace <your_pipeline_name>). The airflow will send ds (rthe execution date as YYYY-MM-DD) to `etl_date` as kedro parameter.
```python
from collections import defaultdict

from pathlib import Path

from airflow import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from datetime import datetime

from kedro.framework.session import KedroSession

import sys
import os
sys.path.append(os.getcwd())
sys.path.append('/code/etl-pipeline')

from kedro.framework.startup import bootstrap_project

class KedroOperator(BaseOperator):

    @apply_defaults
    def __init__(
        self,
        package_name: str,
        pipeline_name: str,
        node_name: str,
        project_path: str,
        env: str,
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.package_name = package_name
        self.pipeline_name = pipeline_name
        self.node_name = node_name
        self.project_path = project_path
        self.env = env

    def execute(self, context):
        bootstrap_project(project_path)
        
        etl_date = context["ds"]
        
        with KedroSession.create(
            self.project_path, 
            env=self.env,
            extra_params={
                'etl_date': etl_date
            }
        ) as session:
            session.run(
                self.pipeline_name,
                node_names=[self.node_name],
                # runner=WriteFunctionLogRunner(),
            )

# Kedro settings required to run your pipeline
env = "local"
pipeline_name = "<your_pipeline_name>"
project_path = Path.cwd()
package_name = "etl_pipeline"

# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5)
}

# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG(
    "<your_pipeline_name>",
    start_date=datetime(2019, 1, 1),
    max_active_runs=3,
    schedule_interval="0 17 * * *",  # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
    default_args=default_args,
    tags=["de-pipeline"],
    catchup=False # enable if you don't want historical dag runs to run
) as dag:
    ...
```

4. create .env file
```
PROJECT_NAME=<YOUR_PROJECT_NAME>
```
5. run Airflow with docker compose
```
cd airflow
docker compose up --build
```

6. go to localhost:8084 and login with default username and password

## FAQ
if you have problem with folder permission, use this following command
```sh
sudo chgrp -R root * && sudo chmod -R 770 *
```



## With Write Logs (Old)
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