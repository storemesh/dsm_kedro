# Daily Update Guide

## For overwrite everyday
1. go to `src/config/project_setting.py`. Set ETL_MODE to this

```python
...
ETL_MODE = {
    'DsmDataNode': {
        'write': {
            # mode have two choice
            # - initial: overwrite parquet file
            # - append: append parquet file with partition. auto_partition must be set to True for this.
            'mode': 'initial', 
            'append_folder': ['Integration'],  # only for append
            'auto_partition': False, # generate '_retrieve_date' column (from params:etl_date) and use it as partition
        },
    },
    'DsmListDataNode': {
        'read': {  # for list datanode only
            # mode have two choice
            # - from_date: read datanode that same with etl_date from parameter. Fail if that date it's not exist in list datanode
            # - latest: use latest datanode in list
            'mode': 'latest', 
            'load_only_updated': False,   
            'list_datanode_folder': ['Landing'],  
        },
        'write': {
            # mode have two choice
            # - from_date: write datanode that same with etl_date from parameter. overwrite_same_date must be True
            # - latest: write datanode in the end of list
            'mode': 'latest',
            'overwrite_same_date': True
        }
    }
}
...

```

2. Run all pipeline or use airflow as usual



## For append everyday
1. go to `src/config/project_setting.py`. Set ETL_MODE to this

```python
...
ETL_MODE = {
    'DsmDataNode': {
        'write': {
            # mode have two choice
            # - initial: overwrite parquet file
            # - append: append parquet file with partition. auto_partition must be set to True for this.
            'mode': 'append', 
            'append_folder': ['Integration'],  # only for append
            'auto_partition': True, # generate '_retrieve_date' column (from params:etl_date) and use it as partition
        },
    },
    'DsmListDataNode': {
        'read': {  # for list datanode only
            # mode have two choice
            # - from_date: read datanode that same with etl_date from parameter. Fail if that date it's not exist in list datanode
            # - latest: use latest datanode in list
            'mode': 'from_date', 
            'load_only_updated': True, # set to False if you don't want to do hash checking with previous datanode  
            'list_datanode_folder': ['Landing'],  
        },
        'write': {
            # mode have two choice
            # - from_date: write datanode that same with etl_date from parameter. overwrite_same_date must be True
            # - latest: write datanode in the end of list
            'mode': 'from_date',
            'overwrite_same_date': True
        }
    }
}
...

```

2. go to `conf/base/parameters.yml`. add etl_date in the file and set date that you want to test
```yml
# conf/base/parameters.yml

etl_date: <YOUR_DATE in YYYY-MM-DD format>
# for example : etl_date: 2023-07-10
```
3. if you node want to access the date variable, you can use `params:etl_date` as input of pipeline
4. Run all pipeline or use airflow as usual. This is the behavior of each zone
- All ListDataNode in Landing 
  - write: It will write by using etl_date as timestamp (YYYY/MM/DD 00.00.00), not datetimenow. If you write landing node more than one time, it will overwrite the exist one.
  - read: It will read data from etl_date (not latest). If `load_only_updated` is True, it will compare with previous date(data node) and get the update data

  Note: if you don't want to do this to all ListDataNode in Landing, go to dataset that you want in catalog file and set this config manualy. For example

  ```yml
  l.google_news_bbc:
    type: dsm_kedro_plugin.custom_dataset.dsm_dataset.DsmListDataNode
    project_folder_name: Landing
    file_name: google_news_bbc
    credentials: dsmlibrary
    config:
        load_only_updated: False
  ```

- All DsmDataNode in Integration
  - write : It will create new column that name `_retrieve_date` and save it in append mode by using this column for partitioning

  Note: if you don't want to do this to all DsmDataNode in Integration, go to dataset that you want in catalog file and set this config manualy. For example

  ```yml
  i.google_news_bbc:
    type: dsm_kedro_plugin.custom_dataset.dsm_dataset.DsmDataNode
    project_folder_name: Integration
    file_name: google_news_bbc
    credentials: dsmlibrary
    write_extra_param: {
      append: False,
      partition_on: my_date_column,
    }
  ```
### Run with airflow
You can test backfill or daily update by following these step
1. follow this step for running airflow [airflow.md](airflow.md)
2. after deploy airflow, go to pipeline that you want
3. click run button and click `Trigger DAG w/ config`
4. select date that you want to run
5. see result

