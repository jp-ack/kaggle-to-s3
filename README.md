# Kaggle Data Controller 1.0
This program will serve as a component in an ETL pipeline , by using the kaggle API to pull datasets from the web , and directly send them into an s3 bucket.

## Requirements 
This program requires 2 things before it can work properly:
        -You have an AWS s3 bucket (which you have access to) , See 'S3 Help' Below
        -You have a kaggle API key. This , in short , is a JSON file provided by kaggle and must be stored in your
         home folder as ./kaggle ( See Kaggle help below)

## Requirement (1/2) AWS S3 Configuration 
S3 buckets are nothing more than an elastic file share. The code can be modified to not require an S3 bucket , but for the scope of this project: 
- Create an AWS account , (s3 buckets offer up to 5 gb of storage for free.) 
- Create an S3 bucket ( There are many comprehensive tutorials online , and although many of you will be able to figure it out on your own , here is the
 documentation https://docs.aws.amazon.com/s3/ ) 
- Be sure to follow the proper S3 naming conventions , names are unique by the area. (IE , all names in us-east-1 are unique , but not unique to us-west-1) 
- The program will prompt you for the name of your bucket. 
- Once you have created an AWS account , generate a secret and private access key, save these (as you may use them for future projects) 
- Run the following command  
    ```bash 
    aws configure
    ```
- Enter in your secret and private access key. do not share these with anyone else. 
- Enter in your region that your S3 bucket is configured to 
- Enter 'json' for format 
- You are finished this step. 
## Kaggle Configuration
https://www.kaggle.com/docs/api#getting-started-installation-&-authentication
NOTE : You MUST have a kaggle account (completely free)
This link will guide you in 
- Generating a kaggle.json file , which will sit in your home directory as ~/.kaggle/kaggle.json 
- the Kaggle api will not function unless you completed the step above 
    ### (Requirement 2/2) Kaggle Instructions  
- Sign up for Kaggle.com account, kaggle.com 
        - ~/.kaggle/kaggle.json  <-- contains your api key generated from the www.kaggle.com/settings/account page and create a token.  
        - The kaggle dependecy will be packaged into this repository , so in theory , you should NOT need to run  
    ```bash
    pip install kaggle. 0_0
    ```       
## Version 1.0 goals
In the first release of this software , we will be sure to include
    - Ability to write-in the name of the user and their dataset to use
    - Ability to use s3 bucket ,
    - Pytest unit testing to ensure reliability and secure transfer of data
