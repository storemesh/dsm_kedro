from typing import Dict

from kedro.pipeline import Pipeline
from basic_kedro.pipelines.merge_data import pipeline as md 

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    merge_data_pipeline = md.create_pipeline()

    return {
        "__default__": merge_data_pipeline,
        "merge_data": merge_data_pipeline,
    }