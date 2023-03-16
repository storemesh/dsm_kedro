"""
This is a boilerplate pipeline 'db1_fact_exporter'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import dim_exporter_merge

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
      [        
          node(
            func=dim_exporter_merge,
            inputs=dict(
                db1_dim_exporter = "s.db1_dim_exporter",
                db2_dim_exporter = "s.db2_dim_exporter",
            ),
            outputs = "i.dim_exporter",
            name = "dim_exporter_merge",
          ),
      ]
    )