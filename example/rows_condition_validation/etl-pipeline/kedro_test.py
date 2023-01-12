from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project
from kedro.framework.startup import bootstrap_project
from src.dsm_kedro_plugin.custom_runner.dsm_runner import WriteFunctionLogRunner
from kedro.runner import SequentialRunner
from pathlib import Path

# package_name = 
# project_path = 
# env =
# node_name =
# pipeline_name =

env = "local"
pipeline_name = "Payment"
project_path = Path.cwd()
package_name = "etl_pipeline"
node_name = "staging___system01___myapp_payment___node"

bootstrap_project(project_path)
# configure_project(package_name)
with KedroSession.create(
    # package_name,
        project_path=project_path,
        env=env,
        extra_params={
                    "pipeline_name": pipeline_name
                 }
    ) as session:
    print('----------TT-------------')
    print(project_path)
    context = session.load_context()
    # import pdb; pdb.set_trace()
    session.run(pipeline_name, node_names=[node_name], runner=WriteFunctionLogRunner())