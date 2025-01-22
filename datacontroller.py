# this program will serve as a local interface to upload files to a specified s3 bucket
# Author : Jean - Pierre Martinez
# Date : 1/21/2025
# "What i cannot create , i do not understand " - Richard Feynman
# lets use nicegui
# We will pull from Kaggle, briefly storing data in memory , And upload into an AWS s3 Bucket. 
# DATASET : https://www.kaggle.com/datasets/ashaychoudhary/heart-attack-in-youth-vs-adult-in-russia

import boto3
from kaggle.api.kaggle_api_extended import KaggleApi
import os

#Step 1. Authenticate with Kaggle 
api = KaggleApi()
api.authenticate()

#Step 2. Specify Dataset File & Bucket
dataset_name = 'ashaychoudhary/heart-attack-in-youth-vs-adult-in-russia' 
dataset_file = 'heart_attack_russia_youth_vs_adult.csv'
## this is what name will be stored into the s3 bucket 
bucket_name = 'kaggledata1'

#Step 3. Self Explanitory 
dataset_destination_folder = './'

#Download the dataset and unzip it into current directory
api.dataset_download_files(dataset_name,path = dataset_destination_folder,unzip=True)

print(f"Sucessfully pulled the datasheet in the form of a zip file and store in local directory ")

#Step 4. Upload dataset to AWS S3
csv_filepath = os.path.join(dataset_destination_folder,dataset_file)

s3_client = boto3.client('s3', region_name='us-east-1')

#Step 5. Upload the file to the S3 bucket
with open(csv_filepath, 'rb') as file_obj:
    s3_client.upload_fileobj(file_obj, bucket_name, dataset_file)

print(f"Dataset '{dataset_file}' uploaded to S3 bucket '{bucket_name}'!")

#Step 6. To optimize memory utilization , we will remove the file locally after it is uploaded to s3.
file_size = os.path.getsize(csv_filepath)
os.remove(csv_filepath)
print(f"Local file '{dataset_file}' deleted to save space. {file_size} bytes deleted")
