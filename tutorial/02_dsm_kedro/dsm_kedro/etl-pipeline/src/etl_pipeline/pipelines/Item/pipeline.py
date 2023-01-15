from kedro.pipeline import Pipeline, node, pipeline
from .nodes import merge_item, staging_app1, staging_app2, to_clickhouse

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # staging
            # app 1
            node(
                func=staging_app1,
                inputs="l.sys1_myapp_item",
                outputs="s.sys1_myapp_item",
                name="staging_app1_node",
            ),

            # app 2
            node(
                func=staging_app2,
                inputs="l.sys2_myapp_product",
                outputs="s.sys2_myapp_product",
                name="staging_app2_node",
            ),
            
            # integration
            node(
                func=merge_item,
                inputs=dict(
                    data_app1="s.sys1_myapp_item", 
                    data_app2="s.sys2_myapp_product",
                ),
                outputs="i.item",
                name="merge_item_node",
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