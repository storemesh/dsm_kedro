from kedro.pipeline import Pipeline, node, pipeline
from .nodes import merge_item, staging_app1, staging_app2, to_clickhouse

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # staging
            # app 1
            node(
                func=staging_app1,
                inputs="landing___system01___myapp_item",
                outputs="staging___system01___myapp_item",
                name="staging___system01___myapp_item____node",
            ),

            # app 2
            node(
                func=staging_app2,
                inputs="landing___system02___myapp_product",
                outputs="staging___system02___myapp_product",
                name="staging___system02___myapp_product___node",
            ),
            
            # integration
            node(
                func=merge_item,
                inputs=dict(
                    data_app1="staging___system01___myapp_item", 
                    data_app2="staging___system02___myapp_product",
                ),
                outputs="integration___Item",
                name="integration___Item___node",
            ),

            # # clickhouse
            # node(
            #     func=to_clickhouse,
            #     inputs="integration___Item", 
            #     outputs="clickhouse___Item",
            #     name="clickhouse___Item___node",
            # ),

        ]
    )