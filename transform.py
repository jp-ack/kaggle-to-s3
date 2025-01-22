# ALL THIS DOES IS RETURN THE DATA FROM THE S3 BUCKET 
import boto3
import pandas as pd
from io import StringIO

def pull_from_s3(bucket,dataset_file_name): 
    pd.set_option('display.max_columns', None)
    print(f"Starting pull_from_s3()...", flush = True)

    s3_client = boto3.client('s3',region_name = 'us-east-1')

    bucket_name = bucket
    file_key = dataset_file_name ## the file in the s3 bucket

    response = s3_client.get_object(Bucket = bucket_name, Key = file_key)
    csv_data = response['Body'].read().decode('ISO-8859-1') # change from utf-8
    print(f"succesfully grabbed response from S3 source : {bucket_name}", flush = True)
    #Load csv into a pandas DataFrame
    data = pd.read_csv(StringIO(csv_data))

    return data

