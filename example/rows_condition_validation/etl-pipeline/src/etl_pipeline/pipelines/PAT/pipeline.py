from kedro.pipeline import Pipeline, node, pipeline
from .nodes import TM_preprocess, PAT_preprocess

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [           
            # staging
            node(
                func=PAT_preprocess,
                inputs="landing___PAT",
                outputs="integration___PAT",
                name="integration___PAT___node",
            ),
        ]
    )