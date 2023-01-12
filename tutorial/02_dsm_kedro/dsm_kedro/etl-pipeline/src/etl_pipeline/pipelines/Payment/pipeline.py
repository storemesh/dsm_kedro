"""
This is a boilerplate pipeline 'payment_integration'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from ..utils import func_pass_data, merge_two_source
from .nodes import staging_app1, staging_app2

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [             
            # staging
            node(
                func=staging_app1,
                inputs="landing___system01___myapp_payment",
                outputs="staging___system01___myapp_payment",
                name="staging___system01___myapp_payment___node",
            ),
            node(
                func=staging_app2,
                inputs="landing___system02___myapp_payment",
                outputs="staging___system02___myapp_payment",
                name="staging___system02___myapp_payment___node",
            ),
            
            # integration
            node(
                func=merge_two_source,
                inputs=["staging___system01___myapp_payment", "staging___system02___myapp_payment"],
                outputs="integration___Payment",
                name="integration___Payment___node",
            ),

        ]
    )
