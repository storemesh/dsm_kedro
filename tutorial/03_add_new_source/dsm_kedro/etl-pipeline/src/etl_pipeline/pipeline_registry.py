"""Project pipelines."""
from typing import Dict

import sys
import os
sys.path.append(os.getcwd())

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline, pipeline
from src.etl_pipeline.pipelines.query_landing import pipeline as query_landing_obj   

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    query_landing_pipeline = query_landing_obj.create_pipeline()

    return {
        "__default__": pipeline([]),
        "query_landing": query_landing_pipeline,
    }


