from kedro.pipeline import Pipeline, node, pipeline
from .nodes import to_ckan_TM, to_ckan_PAT

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [           
            node(
                func=to_ckan_TM,
                inputs=dict(
                    data="integration___TM",
                    ckan_parameter="params:ckan_parameter"
                ),
                outputs=None,
                name="to_ckan___TM___node",
            ),
            
            node(
                func=to_ckan_PAT,
                inputs=dict(
                    data="integration___PAT",
                    ckan_parameter="params:ckan_parameter"
                ),
                outputs=None,
                name="to_ckan___PAT___node",
            ),
        ]
    )