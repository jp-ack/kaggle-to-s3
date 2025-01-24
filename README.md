# Data Controller 1.0
This program will serve as a component in an ETL pipeline , by using the kaggle API to pull datasets from the web , and directly send them into an s3 bucket.

## Requirements
For this program to effectively pull data from a kaggle.com source , store it in an amazon S3 bucket , and return it as "data",
you must ensure the following :
        -You have an AWS s3 bucket (which you have access to) , See 'S3 Help' Below
        -You have a kaggle API key. This , in short , is a JSON file provided by kaggle and must be stored in your
         home folder as ./kaggle ( See Kaggle help below)

## S3 Configuration
    aws.com
## Kaggle Configuration
    Kaggle.com

## Version 1.0 goals
In the first release of this software , we will be sure to include
    - Ability to write-in the name of the user and his/her dataset to use
    - Ability to use s3 bucket ,
    - Testing to ensure reliability and secure transfer of data

## Future Improvements
I later plan to create a capabilities to allow users to use prefix in the cli to specify if they want a copy of said dataset in a specified golder


