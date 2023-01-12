import dask.dataframe as dd
from typing import List, Tuple
import logging

logging.basicConfig()
logger = logging.getLogger('kedro')

def staging_app1(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, file_id = data
    ddf = ddf.reset_index()
    ddf['id'] = 'system01' + '_' + ddf['id'].astype(str) 
    lineage_id = [file_id]
    return (ddf, lineage_id)

def staging_app2(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, file_id = data
    ddf = ddf.reset_index()
    ddf['id'] = 'system02' + '_' + ddf['id'].astype(str) 
    lineage_id = [file_id]
    return (ddf, lineage_id)

def merge_item(
        data_app1: Tuple[dd.DataFrame, int],
        data_app2: Tuple[dd.DataFrame, int],
    ):
    ddf_app1, app1_fid = data_app1
    ddf_app2, app2_fid = data_app2

    all_merge = dd.concat([ddf_app1, ddf_app2])
    all_merge['id'] = all_merge['id'].astype('string')
    
    logger.info(all_merge)

    lineage_id = [app1_fid, app2_fid]
    return (all_merge, lineage_id)


def to_clickhouse(data: Tuple[dd.DataFrame, int]):
    ddf, file_id = data
    return ddf
    