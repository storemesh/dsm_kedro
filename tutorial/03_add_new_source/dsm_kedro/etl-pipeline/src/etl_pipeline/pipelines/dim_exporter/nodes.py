"""
This is a boilerplate pipeline 'db1_fact_exporter'
generated using Kedro 0.18.4
"""

import dask.dataframe as dd
from datetime import datetime
from typing import List, Tuple

def dim_exporter_merge(
        db1_dim_exporter: Tuple[dd.DataFrame, int],
        db2_dim_exporter: Tuple[dd.DataFrame, int],
    ) -> Tuple[dd.DataFrame, List[int]] :    
    ddf_db1_dim_exporter, meta_db1_dim_exporter = db1_dim_exporter
    ddf_db2_dim_exporter, meta_db2_dim_exporter = db2_dim_exporter
    
    ddf = dd.concat([
        ddf_db1_dim_exporter,
        ddf_db2_dim_exporter,
    ])
    
    lineage_id = [meta_db1_dim_exporter, meta_db2_dim_exporter]
    return (ddf, lineage_id)
