# this will serve as the user - input module for powering this application
# AWS credentials must be fulfilled 
# the kaggle dataset you call must exist
# i want to be able to TYPE the name of the dataset name , and the name of the csv 'this name '
from transform import pull_from_s3
import transform
import datacontroller


def main():
    
    #ask user for what file they want and feed it into the datacontroller method
    #kaggle_user_info = str(input("type name of bucket: user/data"))
    #dataset_file_name = str(input("please type in the name of the csv"))
    
    print("Welcome to Kaggle Data Controller interface , LUX Software 2025")
    dataset_publisher= str(input("please enter the name of the data scientist and page , john/datapage :")) 
    dataset_file_name = str(input("please input the name of the csv file in the publishers page :"))
    bucket = str(input("specify the name of your aws bucket ex : kaggledata1 :"))
    
    #pushes data to s3 bucket 
    datacontroller.source_from_kaggle(dataset_publisher,dataset_file_name,bucket)
    
    #pulls data down from s3 bucket to work with
    data = transform.pull_from_s3(bucket,dataset_file_name)
    
    #print if data is returned 
    
    print(data.head(20))
   

main()