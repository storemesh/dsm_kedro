"""Project pipelines."""
from typing import Dict

import sys
import os
sys.path.append(os.getcwd())

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline, pipeline
from src.etl_pipeline.pipelines.PAT import pipeline as PAT_obj
from src.etl_pipeline.pipelines.TM import pipeline as TM_obj
from src.etl_pipeline.pipelines.to_ckan import pipeline as to_ckan_obj

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    PAT_pipeline = PAT_obj.create_pipeline()
    TM_pipeline = TM_obj.create_pipeline()
    to_ckan_pipeline = to_ckan_obj.create_pipeline()
    
    return {
        "__default__": pipeline([]),
        "PAT": PAT_pipeline,
        "TM": TM_pipeline,
        "to_ckan": to_ckan_pipeline,
    }


