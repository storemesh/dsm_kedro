"""
This is a boilerplate pipeline 'db1_fact_exporter'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import db1_preprocess

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
      [        
          node(
            func=db1_preprocess,
            inputs=dict(
                df_db1 = "l.db1_exporter",
            ),
            outputs = "s.db1_dim_exporter",
            name = "db1_preprocess",
          ),
      ]
    )