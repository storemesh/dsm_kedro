from collections import defaultdict

from pathlib import Path

from airflow import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.version import version
from datetime import datetime, timedelta

from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project

import sys
import os
sys.path.append(os.getcwd())

from airflow.operators.python_operator import PythonOperator
from kedro.framework.startup import bootstrap_project
from src.dsm_kedro_plugin.custom_runner.dsm_runner import WriteFunctionLogRunner
from src.dsm_kedro_plugin.custom_runner.utils.logs_generator import gen_log_start, gen_log_finish

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
        with KedroSession.create(self.project_path, env=self.env) as session:
            session.run(
                self.pipeline_name,
                 node_names=[self.node_name],
                 runner=WriteFunctionLogRunner(),
            )

# Kedro settings required to run your pipeline
env = "local"
pipeline_name = "Payment"
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
    "Payment_dags",
    start_date=datetime(2019, 1, 1),
    max_active_runs=3,
    schedule_interval="0 0 * * *",  # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
    default_args=default_args,
    catchup=False # enable if you don't want historical dag runs to run
) as dag:

    tasks = {}

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

    tasks["staging-system01-myapp-payment-node"] = KedroOperator(
        task_id="staging-system01-myapp-payment-node",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="staging___system01___myapp_payment___node",
        project_path=project_path,
        env=env,
    )

    tasks["staging-system02-myapp-payment-node"] = KedroOperator(
        task_id="staging-system02-myapp-payment-node",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="staging___system02___myapp_payment___node",
        project_path=project_path,
        env=env,
    )

    tasks["integration-payment-node"] = KedroOperator(
        task_id="integration-payment-node",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="integration___Payment___node",
        project_path=project_path,
        env=env,
    )

    tasks["start_node"] >> [tasks["staging-system01-myapp-payment-node"], tasks["staging-system02-myapp-payment-node"]]

    tasks["staging-system01-myapp-payment-node"] >> tasks["integration-payment-node"]

    tasks["staging-system02-myapp-payment-node"] >> tasks["integration-payment-node"]

    tasks["integration-payment-node"] >> tasks["end_node"]