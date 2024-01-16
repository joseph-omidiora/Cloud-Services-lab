# language: Python 3.8
import boto3
import os

# Prompt the user for AWS access key, secret key and region
aws_access_key_id = os.environ['aws_access_key_id'] 
aws_secret_access_key = os.environ['aws_secret_access_key']
aws_region = input("Enter your AWS region (default: eu-north-1): ")


# Specify your S3 bucket name
bucket_name = input("Enter your bucket name: ")  

# Specify the local file path you want to upload
local_file_path = 'file.txt'

# Specify the key (object name) under which the file will be stored in the bucket
s3_key = 'prog-storage/file.txt'  # Change this to your desired S3 key

# Create an S3 client
s3 = boto3.client('s3', region_name=aws_region, aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Upload the file to the S3 bucket
try:
    s3.upload_file(local_file_path, bucket_name, s3_key)
    print(f"File uploaded successfully to S3 bucket: {bucket_name}/{s3_key}")
except Exception as e:
    print(f"Error uploading file to S3 bucket: {e}")