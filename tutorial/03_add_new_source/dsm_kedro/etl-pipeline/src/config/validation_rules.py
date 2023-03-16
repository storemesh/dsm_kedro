import dask.dataframe as dd
import pandas as pd
import pandera as pa
from pandera.typing.dask import DataFrame, Series
from dsmlibrary.datanode import DataNode

from src.dsm_kedro_plugin.generate_datanode.utils.utils import get_token
from src.config.project_setting import DATAPLATFORM_API_URI, OBJECT_STORAGE_URI, PROJECT_FOLDER_ID, OBJECT_STORAGE_SECUE

df_master = pd.DataFrame(list(range(14, 100000)), columns=['data'])
ddf_master = dd.from_pandas(df_master, npartitions=3)

token = get_token()
datanode = DataNode(
        token,
        dataplatform_api_uri=DATAPLATFORM_API_URI,
        object_storage_uri=OBJECT_STORAGE_URI,
        object_storage_secue=OBJECT_STORAGE_SECUE,
)

fk_personentity = datanode.read_ddf(file_id=2495)

# define check function with dask
def in_master_table1(series):
    return series.isin(ddf_master['data'].compute())

def fk_personentity(series):
    return series.isin(fk_personentity['id'].compute())
    



def in_number(series):
    return series.isin([1,2,3])

def in_str_dummy(series):
    return series.isin(['str1', 'str2'])

# format: check รูปแบบถูกไหม
# consistency: เช็ค fk
# completeness: เช็ค null

# Rule Define
rules = {
    #date_format
    1 : {
        'func': pa.Check.str_matches(pattern="^([0-9]{4})-?(1[0-2]|0[1-9])-?(3[01]|0[1-9]|[12][0-9])$"), 
        'type': 'format',
    },
    #13_digits
    2 : {
        'func': pa.Check.str_matches(pattern="\d{13}"),
        'type': 'format',
    },
    #phone
    3 : {
        'func':pa.Check.str_matches(pattern="\d{10}"),
        'type': 'format',
    },
    #email
    4 : {
        'func':pa.Check.str_matches(pattern="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"),
        'type': 'format',
    },
    #number
    5 : {
        'func':pa.Check.str_matches(pattern="([0-9]*[.])?[0-9]+"),
        'type': 'format',
    },
    #FK Personentity
    6 : {
        'func':pa.Check(fk_personentity),
        'type': 'consistency',
    }
}