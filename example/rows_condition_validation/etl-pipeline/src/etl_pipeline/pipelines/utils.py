import dask.dataframe as dd
from typing import List, Tuple

def func_pass_data(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, fid = data  

    lineage_id = [fid]
    return (ddf, lineage_id)

def merge_two_source(
    data_app1: Tuple[dd.DataFrame, int], 
    data_app2: Tuple[dd.DataFrame, int]
) -> Tuple[dd.DataFrame, List[int]]:
    ddf_app1, app1_fid = data_app1
    ddf_app2, app2_fid = data_app2
    all_merge = dd.concat([ddf_app1, ddf_app2])    

    lineage_id = [app1_fid, app2_fid]
    return (all_merge, lineage_id)
