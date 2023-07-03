# Script

## landing and integration report
to generate landing and integration report to data discovery. please follow the instruction below
- create `Report` folder in data discovery
- create `conf/base/catalogs/manual/report.yml`
- add this to catalog file
```yml
report.integration_report:
  type: dsm_kedro_plugin.custom_dataset.dsm_dataset.DsmDataNode
  project_folder_name: Report
  file_name: integration_report
  credentials: dsmlibrary

report.landing_report:
  type: dsm_kedro_plugin.custom_dataset.dsm_dataset.DsmDataNode
  project_folder_name: Report
  file_name: landing_report
  credentials: dsmlibrary
```
run code to generate result
- generate landing report
```sh
# dsm_kedro/etl-pipeline 
python src/dsm_kedro_plugin/script/landing_report.py
```
- generate integration report
```sh
# dsm_kedro/etl-pipeline 
python src/dsm_kedro_plugin/script/integration_report.py
```

## Validate Integration file with Data Product
script to check data product sheet with integration indiscovery. It will check consisten of data type, columns name.

step
1. all integration dataset need to be declared in `conf/base/catalogs/manual/integration.yml` 
2. you must have `conf/local/service_account.json` for getting google sheet data (check how to gen credential https://www.youtube.com/watch?v=bu5wXjz2KvU)

how to run
```sh
python src/dsm_kedro_plugin/check_data_product.py -gsheet_fname <ชื่อไฟล์ google sheet>