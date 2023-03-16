REQUIRED_FOLDER_LIST = ["SQLDataNode", "Landing", "Staging", "Integration", "Logs"]

PROJECT_NAME = "tutorial_admin" # (It must be exactly the same value in Project Table of Data Discovery, use it for generate logs)  
PROJECT_FOLDER_ID = 317

DATAPLATFORM_API_URI = "http://10.8.98.55:8000" # example: "https://api.discovery.dev.data.storemesh.com"
OBJECT_STORAGE_URI = "10.8.98.55:9000" # example: "dataframe.objectstorage.dev.data.storemesh.com"

OBJECT_STORAGE_SECUE = False # use True if Object Storage connect with https