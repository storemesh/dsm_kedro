"""
This is a boilerplate pipeline 'order_item_integration'
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
                inputs="landing___system01___myapp_orderitem",
                outputs="staging___system01___myapp_orderitem",
                name="staging___system01___myapp_orderitem___node",
            ),
            node(
                func=staging_app2,
                inputs="landing___system02___myapp_orderitem",
                outputs="staging___system02___myapp_orderitem",
                name="staging___system02___myapp_orderitem___node",
            ),
            
            # integration
            node(
                func=merge_two_source,
                inputs=["staging___system01___myapp_orderitem", "staging___system02___myapp_orderitem"],
                outputs="integration___Orderitem",
                name="integration___Orderitem___node",
            ),
        ]           
    )
