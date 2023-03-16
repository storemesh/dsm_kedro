"""
This is a boilerplate pipeline 'db1_fact_exporter'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import db2_preprocess

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
      [        
          node(
            func=db2_preprocess,
            inputs=dict(
                df_db2 = "l.db2_exporter",
            ),
            outputs = "s.db2_dim_exporter",
            name = "db2_preprocess",
          ),
      ]
    )