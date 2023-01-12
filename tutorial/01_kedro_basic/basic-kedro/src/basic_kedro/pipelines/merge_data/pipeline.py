from kedro.pipeline import Pipeline, node, pipeline
from .nodes import merge_item, merge_order, merge_all

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=merge_item,
                inputs=["item_detail", "shops"],
                outputs="item_shop_merge",
                name="item_shop_merge___node",
            ),
            node(
                func=merge_order,
                inputs=["order", "user"],
                outputs="order_user_merge",
                name="order_user_merge___node",
            ),
            node(
                func=merge_all,
                inputs=["item_shop_merge", "order_user_merge"],
                outputs="result_table",
                name="result_table___node",
            )
        ]
    )