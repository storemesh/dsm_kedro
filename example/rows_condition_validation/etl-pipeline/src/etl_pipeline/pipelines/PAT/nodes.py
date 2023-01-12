import dask.dataframe as dd
from typing import List, Tuple

def TM_preprocess(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, meta = data
    
    ddf['FILING_DATE'] = ddf['FILING_DATE'].astype('M8[us]')
    ddf['REGISTRATION_DATE'] = ddf['REGISTRATION_DATE'].astype('M8[us]')
    ddf['STATUS_DATE'] = ddf['STATUS_DATE'].astype('M8[us]')
    ddf['EXPIRE_DATE'] = ddf['EXPIRE_DATE'].astype('M8[us]')
    
    ddf['REG_NO'] = ddf['REG_NO'].astype('string')
    
    lineage_id = [meta]
    return (ddf, lineage_id)

def PAT_preprocess(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, meta = data
    
    # ddf['FRM_SUBMIT_DATE'] = ddf['FRM_SUBMIT_DATE'].astype('M8[us]')
    # ddf['RECEIVE_DATE'] = ddf['RECEIVE_DATE'].astype('M8[us]')
    # ddf['PUBLICDATE'] = ddf['PUBLICDATE'].astype('M8[us]')
    # ddf['PATENTDATE'] = ddf['PATENTDATE'].astype('M8[us]')
    
    ddf['APP_NO'] = ddf['APP_NO'].astype('string')
    ddf['PUBLICNO'] = ddf['PUBLICNO'].astype('string')
    ddf['PCTNO'] = ddf['PCTNO'].astype('string')
    ddf['PCT'] = ddf['PCT'].astype('string')
    ddf['NAME'] = ddf['NAME'].astype('string')
    ddf['SUBMIT_TYPE'] = ddf['SUBMIT_TYPE'].astype('string')
    
    ddf['FRM_SUBMIT_DATE'] = dd.to_datetime(ddf['FRM_SUBMIT_DATE'], errors='coerce')
    ddf['RECEIVE_DATE'] = dd.to_datetime(ddf['RECEIVE_DATE'], errors='coerce')
    ddf['PUBLICDATE'] = dd.to_datetime(ddf['PUBLICDATE'], errors='coerce')
    ddf['PATENTDATE'] = dd.to_datetime(ddf['PATENTDATE'], errors='coerce')
    
    lineage_id = [meta]
    return (ddf, lineage_id)