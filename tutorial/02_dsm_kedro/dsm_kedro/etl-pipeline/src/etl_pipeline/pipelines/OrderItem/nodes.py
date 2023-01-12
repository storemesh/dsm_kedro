"""
This is a boilerplate pipeline 'order_item_integration'
generated using Kedro 0.18.2
"""

import dask.dataframe as dd
from typing import List, Tuple

def staging_app1(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, file_id = data

    columns = ['id', 'quantity', 'item_id', 'order_id']
    ddf = ddf.reset_index()
    ddf['id'] = f'system01_' + ddf['id'].astype(str)
    ddf['item_id'] = f'system01_' + ddf['item_id'].astype(str)
    ddf['order_id'] = f'system01_' + ddf['order_id'].astype(str)
    ddf = ddf[columns]

    lineage_id = [file_id]
    return (ddf, lineage_id)

def staging_app2(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, file_id = data

    columns = ['id', 'quantity', 'product_id', 'order_id']
    ddf = ddf.reset_index()
    ddf['id'] = f'system02_' + ddf['id'].astype(str)
    ddf['product_id'] = f'system02_' + ddf['product_id'].astype(str)
    ddf['order_id'] = f'system02_' + ddf['order_id'].astype(str)
    ddf = ddf[columns]
    ddf = ddf.rename(columns={'product_id': 'item_id'}) 

    lineage_id = [file_id]
    return (ddf, lineage_id)

