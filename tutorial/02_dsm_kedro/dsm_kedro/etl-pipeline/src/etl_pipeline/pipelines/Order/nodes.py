"""
This is a boilerplate pipeline 'order_integration'
generated using Kedro 0.18.2
"""
import dask.dataframe as dd
from typing import List, Tuple

# def get_order_datetime(ddf: dd.DataFrame, app_name: str) -> dd.DataFrame:
#     columns = ['id', 'created']
#     ddf = ddf.reset_index()
#     ddf['id'] = f'{app_name}_' + ddf['id'].astype(str)
#     ddf['created'] = ddf['created'].astype('M8[us]')
#     results = ddf[columns]
#     return results

# def get_order_datetime_app1(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
#     ddf, file_id = data
#     ddf = get_order_datetime(ddf, "app1")
#     lineage_id = [file_id]
#     return (ddf, lineage_id)

# def get_order_datetime_app2(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
#     ddf, file_id = data
#     ddf = get_order_datetime(ddf, "app2")
#     lineage_id = [file_id]
#     return (ddf, lineage_id)

def staging_app1(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, file_id = data
    ddf = ddf.reset_index()
    ddf['id'] = 'system01' + '_' + ddf['id'].astype(str) 
    ddf['created'] = ddf['created'].astype('M8[us]')
    lineage_id = [file_id]
    return (ddf, lineage_id)


def staging_app2(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, file_id = data
    ddf = ddf.reset_index()
    ddf['id'] = 'system02' + '_' + ddf['id'].astype(str) 
    ddf['created'] = ddf['created'].astype('M8[us]')
    lineage_id = [file_id]
    return (ddf, lineage_id)
