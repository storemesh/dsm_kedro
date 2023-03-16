"""
This is a boilerplate pipeline 'db1_fact_exporter'
generated using Kedro 0.18.4
"""

import dask.dataframe as dd
from datetime import datetime
from typing import List, Tuple

def db1_preprocess(df_db1: dd.DataFrame) -> Tuple[dd.DataFrame, List[int]] :    
    ddf = dd.from_pandas(df_db1, npartitions=1)
    ddf['id'] = 'db1_' + ddf['tax_no']
    ddf['source_pk'] = ddf['tax_no']
    ddf['source_app'] = 'db_1'
    
    lineage_id = []
    return (ddf, lineage_id)
