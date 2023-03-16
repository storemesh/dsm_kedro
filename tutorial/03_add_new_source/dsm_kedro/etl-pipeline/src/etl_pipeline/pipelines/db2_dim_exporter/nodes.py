"""
This is a boilerplate pipeline 'db1_fact_exporter'
generated using Kedro 0.18.4
"""

import dask.dataframe as dd
from datetime import datetime
from typing import List, Tuple

def db2_preprocess(df_db2: dd.DataFrame) -> Tuple[dd.DataFrame, List[int]] :    
    df_db2 = df_db2.rename(columns={'title': 'name'})
    ddf = dd.from_pandas(df_db2, npartitions=1)
    ddf['id'] = 'db2_' + ddf['tax_no']
    ddf['source_pk'] = ddf['tax_no']
    ddf['source_app'] = 'db_2'
    
    lineage_id = []
    return (ddf, lineage_id)
