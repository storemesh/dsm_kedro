"""
This is a boilerplate pipeline 'payment_integration'
generated using Kedro 0.18.2
"""
import dask.dataframe as dd
from typing import List, Tuple

def get_payment_cost(ddf: dd.DataFrame, app_name: str) -> dd.DataFrame:
    columns = ['id', 'amount','created']
    ddf = ddf.reset_index()
    ddf['id'] = f'{app_name}_' + ddf['id'].astype(str)
    ddf['created'] = ddf['created'].astype('M8[us]')
    results = ddf[columns]
    return results

def staging_app1(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, meta = data
    ddf = get_payment_cost(ddf, "system01")
    meta_list = [meta]
    return (ddf, meta_list)

def staging_app2(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, meta = data
    ddf = get_payment_cost(ddf, "system02")
    meta_list = [meta]
    return (ddf, meta_list)
