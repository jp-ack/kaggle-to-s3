import boto3
import pandas as pd
from io import StringIO
def pull_from_s3():
    s3_client = boto3.client('s3',region_name = 'us-east-1')

    bucket_name = 'kaggledata1'
    file_key = 'heart_attack_russia_youth_vs_adult.csv' ## the file in the s3 bucket

    response = s3_client.get_object(Bucket = bucket_name, Key = file_key)
    csv_data = response['Body'].read().decode('utf-8')

    #Load csv into a pandas DataFrame
    data = pd.read_csv(StringIO(csv_data))

    #Display Rows
    ##print(data.head(n = 20))
    return data

