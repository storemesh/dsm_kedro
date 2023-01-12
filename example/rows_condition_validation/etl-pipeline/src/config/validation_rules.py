import dask.dataframe as dd
import pandas as pd
import pandera as pa
from pandera.typing.dask import DataFrame, Series

df_master = pd.DataFrame(list(range(14, 100000)), columns=['data'])
ddf_master = dd.from_pandas(df_master, npartitions=3)

# define check function with dask
def in_master_table1(series):
    return series.isin(ddf_master['data'].compute())

def in_number(series):
    return series.isin([1,2,3])

def in_str_dummy(series):
    return series.isin(['str1', 'str2'])

def get_error_df(df, column_list, failed_index):
    df_result = df.copy()
    df_result.loc[:, :] = True
    df_result.loc[failed_index, column_list] = False
    return df_result

def check_is_unique(series):
    # import pdb;pdb.set_trace()
    # return df['TR_NO'].is_unique
    # import pdb; pdb.set_trace()
    series_value = series #.compute()
    # column_name = series_value.name
    df = series_value.to_frame()
    # duplicate_value = df.duplicated()[column_name]
    # return ~series.isin(duplicate_value)
    return ~df.duplicated(keep=False)
    # return df.is_unique





# find error case
def TM_check_status_code_P(df):
    check_column = ['REG_NO', 'STATUS_CODE']    
    fail_index = (df['REG_NO'].notnull()) & (df['STATUS_CODE'] == 'P')    
    
    df_error = get_error_df(df, check_column, fail_index)  
    return df_error


def TM_check_status_code_R(df):
    check_column = ['STATUS_CODE', 'REG_NO']
    
    fail_index = (df['STATUS_CODE'] == 'R') & (df['REG_NO'].isnull())
    
    df_error = get_error_df(df, check_column, fail_index)  
    return df_error


def TM_check_gaz(df):
    check_column = ['GAZ_NO', 'GAZ_PAGE', 'GAZ_DATE']
    
    df_check = df[check_column]
    count_sum = df_check.isnull().sum(axis=1)
    fail_index = (count_sum >= 1) & (count_sum <= 2)
    
    df_error = get_error_df(df, check_column, fail_index)  
    return df_error


def TM_check_order_date(df):
    check_column = ['FILING_DATE', 'REGISTRATION_DATE', 'STATUS_DATE', 'EXPIRE_DATE']
    
    df_check = df[check_column]
    pass_index = (
        (df_check['FILING_DATE'] <= df_check['REGISTRATION_DATE']) & \
        (df_check['REGISTRATION_DATE'] <= df_check['STATUS_DATE']) & \
        (df_check['STATUS_DATE'] < df_check['EXPIRE_DATE'])
    )
    
    df_error = get_error_df(df, check_column, ~pass_index)  
    return df_error


def TM_check_registration(df):
    check_column = ['REG_NO', 'REGISTRATION_DATE']
    
    fail_index = (df['REG_NO'].notnull()) & (df['REGISTRATION_DATE'].isnull())    

    df_error = get_error_df(df, check_column, fail_index)  
    return df_error


def PAT_check_submit_date(df):
    check_column = ['FRM_SUBMIT_DATE', 'RECEIVE_DATE']
    
    fail_index = (df['FRM_SUBMIT_DATE'].isnull()) | (df['RECEIVE_DATE'].isnull())
    
    df_error = get_error_df(df, check_column, fail_index)  
    return df_error


def PAT_check_public(df):
    df_check = df[['PUBLICNO', 'PUBLICDATE']]
    count_sum = df_check.isnull().sum(axis=1)
    fail_index = (count_sum == 1)
    return ~fail_index

def PAT_check_patent(df):
    df_check = df[['PATENTNO', 'PATENTDATE']]
    count_sum = df_check.isnull().sum(axis=1)
    fail_index = (count_sum == 1)
    return ~fail_index


def PAT_check_order_date(df):
    pass_index = (
        (df['FRM_SUBMIT_DATE'] <= df['RECEIVE_DATE']) & \
        (df['RECEIVE_DATE'] < df['PUBLICDATE']) & \
        (df['PUBLICDATE'] < df['PATENTDATE'])
    )
    return pass_index

def PAT_check_PCT(df):
    fail_index = (df['PCT'] == 'Y') & (df['PCTNO'].isnull())
    return ~fail_index


##
# format: check รูปแบบถูกไหม
# consistency: เช็ค fk
# completeness: เช็ค null


# Rule Define
rules = {
    1 : {
        'func': pa.Check.in_range(min_value=1, max_value=1000),
        'type': 'format',
    },
    2 : {
        'func': pa.Check(in_str_dummy),
        'type': 'consistency',
    },
    3 : {
        'func': pa.Check(in_master_table1),
        'type': 'consistency',
    },
    4 : {
        'func': pa.Check(check_is_unique),
        'type': 'consistency',
    },
    5 : {
        'func': pa.Check(TM_check_status_code_P),
        'type': 'completeness',
    },
    6 : {
        'func': pa.Check(TM_check_status_code_R),
        'type': 'completeness',
    },
    7 : {
        'func': pa.Check(TM_check_gaz),
        'type': 'completeness',
    },
    8 : {
        'func': pa.Check(TM_check_order_date),
        'type': 'format',
    },
    9 : {
        'func': pa.Check(TM_check_registration),
        'type': 'completeness',
    },  
    10 : {
        'func': pa.Check(PAT_check_submit_date),
        'type': 'consistency',
    },  
    11 : {
        'func': pa.Check(PAT_check_public),
        'type': 'consistency',
    },     
    12 : {
        'func': pa.Check(PAT_check_patent),
        'type': 'consistency',
    },    
    13 : {
        'func': pa.Check(PAT_check_order_date),
        'type': 'consistency',
    },       
    14 : {
        'func': pa.Check(PAT_check_PCT),
        'type': 'consistency',
    },          
}