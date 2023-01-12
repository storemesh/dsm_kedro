"""Project pipelines."""
from typing import Dict

import sys
import os
sys.path.append(os.getcwd())

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline, pipeline
from src.etl_pipeline.pipelines.query_landing import pipeline as query_landing_obj
from src.etl_pipeline.pipelines.Item import pipeline as Item_obj
from src.etl_pipeline.pipelines.OrderItem import pipeline as OrderItem_obj
from src.etl_pipeline.pipelines.Order import pipeline as Order_obj
from src.etl_pipeline.pipelines.Payment import pipeline as Payment_obj

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    query_landing_pipeline = query_landing_obj.create_pipeline()
    item_pipeline = Item_obj.create_pipeline()
    orderItem_pipeline = OrderItem_obj.create_pipeline()
    order_pipeline = Order_obj.create_pipeline()
    payment_pipeline = Payment_obj.create_pipeline()

    return {
        "__default__": pipeline([]),
        "query_landing": query_landing_pipeline,
        "Item": item_pipeline,
        "OrderItem": orderItem_pipeline,
        "Order": order_pipeline,
        "Payment": payment_pipeline,
    }


