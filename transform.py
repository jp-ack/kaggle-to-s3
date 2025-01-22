import boto3
import pandas as pd
from io import StringIO
from datacontroller import dataset_file
def pull_from_s3():
    print(f"Starting pull_from_s3()...", flush = True)

    s3_client = boto3.client('s3',region_name = 'us-east-1')

    bucket_name = 'kaggledata1'
    ##file_key = 'heart_attack_russia_youth_vs_adult.csv' ## the file in the s3 bucket
    file_key = dataset_file

    response = s3_client.get_object(Bucket = bucket_name, Key = file_key)
    csv_data = response['Body'].read().decode('utf-8')
    print(f"succesfully grabbed response from S3 source : {bucket_name}", flush = True)
    #Load csv into a pandas DataFrame
    data = pd.read_csv(StringIO(csv_data))

    #Display Rows
    ##print(data.head(n = 20))
    return data

