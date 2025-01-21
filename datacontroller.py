# this program will serve as a local interface to upload files to a specified s3 bucket
# Author : Jean - Pierre Martinez
# Date : 1/21/2025
# "What i cannot create , i do not understand " - Richard Feynman
# lets use nicegui
# We will pull from Kaggle, briefly storing data in memory , And upload into an AWS s3 Bucket. 
# DATASET : https://www.kaggle.com/datasets/ashaychoudhary/heart-attack-in-youth-vs-adult-in-russia

import boto3
from kaggle.api.kaggle_api_extended import KaggleApi
import requests
import zipfile
import io
from io import BytesIO

#Step 1. Authenticate with Kaggle 
api = KaggleApi()
api.authenticate

#Step 2. Specify Dataset File & Bucket
dataset_name = 'ashaychoudhary/heart-attack-in-youth-vs-adult-in-russia' 
dataset_file = 'heart_attack_russia_youth_vs_adult.csv'
bucket_name = 'kaggledata1'

#Step 3. Download set as Zip file into memory 
response = api.dataset_download_files(dataset_name, unzip=True)

#Step 4. Create BytesIO obj to load into mem
zip_file_obj = BytesIO(response)

#Step 5. Unzip the file from memory
with zipfile.ZipFile(zip_file_obj, 'r') as zip_ref:
    with zip_ref.open(dataset_file) as my_file:
        file_obj =BytesIO(my_file.read())
        
#Step 6. set up s3
s3_client = boto3.client('s3',region_name ='us-east-1')   

#Step 7. Upload contents to memory nm 
    