from kedro.pipeline import Pipeline, node, pipeline
from .nodes import TM_preprocess

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [           
            node(
                func=TM_preprocess,
                inputs="landing___TM",
                outputs="integration___TM",
                name="integration___TM___node",
            ),
        ]
    )