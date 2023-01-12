import requests
import json
import dask.dataframe as dd
from typing import List, Tuple, Dict

## create package
def sendMetaToCkan(url_ckan, api_key, ckan_meta):
    headers = {
        'content-type': 'application/json',
        'Authorization': api_key,
    }
    url = 'http://{}/api/action/package_create'.format(url_ckan)
    respond = requests.post(url, data=json.dumps(ckan_meta), headers=headers)
    res_text = respond.content.decode('utf-8').replace('\n','br')
    print(res_text)
    
## Upload File
def uploadFileToCkan(url_ckan, api_key, file_meta, path_input):
    headers = {'X-CKAN-API-Key': api_key}
    url = 'http://{}/api/action/resource_create'.format(url_ckan)
    with open(path_input, "rb") as f:
        form_file = {'upload': f}
        respond = requests.post(url, data=file_meta, headers=headers, files=form_file)
        res_text = respond.content.decode('utf-8').replace('\n','br')
        print(res_text)
        print('<b>File has been uploaded</b>')

def to_ckan_TM(
        data: Tuple[dd.DataFrame, int],
        ckan_parameter: Dict,               
    ) -> None:
    ddf, meta = data
    
    url_ckan = ckan_parameter['url_ckan']
    api_key = ckan_parameter['api_key']
    ckan_meta = {
        "name": "tm",
        "title": "TM",
        "notes": "ข้อมูลเครื่องหมายการค้า",
        "data_type": "ข้อมูลสถิติ",
        "owner_org": "organization01", ## ต้องสร้างองค์กรณ์ก่อนใน ckan และต้องใช้ชื่อ url
        "data_source": "-",
        "maintainer": "-",
        "update_frequency_unit": "ปี",
        "data_format": [
            "CSV"
        ],
        "maintainer_email": "test@gmail.com",
        "objective": [
            "ยุทธศาสตร์ชาติ",
            "แผนพัฒนาเศรษฐกิจและสังคมแห่งชาติ"
        ],
        "data_category": "ข้อมูลสาธารณะ",
        "geo_coverage": "ประเทศ",
        "license_id": "License not specified"
    }
    
    # create dataset
    sendMetaToCkan(url_ckan, api_key, ckan_meta)
        
    # upload data
    file_meta = {
        'package_id': ckan_meta['name'],
        'name': ckan_meta['notes'],
    }
    path_input = f"data/03_primary/{meta['file_name']}.csv"
    ddf.to_csv(path_input, single_file=True)
    
    uploadFileToCkan(url_ckan, api_key, file_meta, path_input)
    
    lineage_id = [meta]
    return (ddf, lineage_id)


def to_ckan_PAT(
        data: Tuple[dd.DataFrame, int],
        ckan_parameter: Dict,               
    ) -> None:
    ddf, meta = data
    
    url_ckan = ckan_parameter['url_ckan']
    api_key = ckan_parameter['api_key']
    ckan_meta = {
        "name": "pat",
        "title": "PAT",
        "notes": "ข้อมูลสิทธิบัตร",
        "data_type": "ข้อมูลสถิติ",
        "owner_org": "organization01", ## ต้องสร้างองค์กรณ์ก่อนใน ckan และต้องใช้ชื่อ url
        "data_source": "-",
        "maintainer": "-",
        "update_frequency_unit": "ปี",
        "data_format": [
            "CSV"
        ],
        "maintainer_email": "test@gmail.com",
        "objective": [
            "ยุทธศาสตร์ชาติ",
            "แผนพัฒนาเศรษฐกิจและสังคมแห่งชาติ"
        ],
        "data_category": "ข้อมูลสาธารณะ",
        "geo_coverage": "ประเทศ",
        "license_id": "License not specified"
    }
    
    # create dataset
    sendMetaToCkan(url_ckan, api_key, ckan_meta)
        
    # upload data
    file_meta = {
        'package_id': ckan_meta['name'],
        'name': ckan_meta['notes'],
    }
    path_input = f"data/03_primary/{meta['file_name']}.csv"
    ddf.to_csv(path_input, single_file=True)
    
    uploadFileToCkan(url_ckan, api_key, file_meta, path_input)
    
    lineage_id = [meta]
    return (ddf, lineage_id)