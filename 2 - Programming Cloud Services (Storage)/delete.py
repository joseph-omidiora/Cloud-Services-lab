#Language: Python 3
import boto3
import os

# Prompt the user for AWS access key and secret key
aws_access_key_id = os.environ['aws_access_key_id'] 
aws_secret_access_key = os.environ['aws_secret_access_key']
aws_region = input("Enter your AWS region (default: eu-north-1): ")

# Initialize the AWS client using the provided credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)


# Specify your S3 bucket name
bucket_name = input("Enter your S3 bucket name: ") 

# Specify the key (object name) under which the file will be stored in the bucket
s3_key_to_delete = input("Specify the key (object name) to delete: ") 

# Create an S3 client
s3 = boto3.client('s3', region_name=aws_region, aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)


# Delete the object from the S3 bucket
try:
    s3.delete_object(Bucket=bucket_name, Key=s3_key_to_delete)
    print(f"Object deleted successfully from S3 bucket: {bucket_name}/{s3_key_to_delete}")
except Exception as e:
    print(f"Error deleting object from S3 bucket: {e}")