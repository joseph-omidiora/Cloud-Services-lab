# language: Python 3.8
import boto3
import os

# Prompt the user for AWS access key, secret key and region
aws_access_key_id = os.environ['aws_access_key_id'] 
aws_secret_access_key = os.environ['aws_secret_access_key']
aws_account_id = os.environ['aws_account_id']


# Initialize the AWS client using the provided credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# Specify your AWS region
region = 'eu-west-1'  # Change this to your desired region

# Create an S3 client
s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# List S3 buckets
try:
    response = s3.list_buckets()
    buckets = response['Buckets']

    print("List of S3 buckets in " + region + ":")
    for bucket in buckets:
        res = s3.get_bucket_location(
            Bucket=bucket['Name'],
            ExpectedBucketOwner="aws_account_id"
            )
        
        if res['LocationConstraint'] == region:
            print(bucket["Name"])

except Exception as e:
    print(f"Error listing S3 buckets: {e}")
