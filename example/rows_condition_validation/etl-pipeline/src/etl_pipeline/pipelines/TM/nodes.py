import dask.dataframe as dd
from typing import List, Tuple
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger('kedro')
logger.setLevel(logging.DEBUG)


def TM_preprocess(data: Tuple[dd.DataFrame, int]) -> Tuple[dd.DataFrame, List[int]]:
    ddf, meta = data
    
    ddf['FILING_DATE'] = ddf['FILING_DATE'].astype('M8[us]')
    ddf['REGISTRATION_DATE'] = ddf['REGISTRATION_DATE'].astype('M8[us]')
    ddf['STATUS_DATE'] = ddf['STATUS_DATE'].astype('M8[us]')
    ddf['EXPIRE_DATE'] = ddf['EXPIRE_DATE'].astype('M8[us]')
    
    ddf['REG_NO'] = ddf['REG_NO'].astype('string')
    
    logger.info('hello from node.py')
    logger.info(ddf)
    lineage_id = [meta]
    return (ddf, lineage_id)
