# language: Python 3.8
import boto3

# Prompt the user for AWS access key, secret key and region
aws_access_key_id = input("Enter your AWS Access Key ID: ")
aws_secret_access_key = input("Enter your AWS Secret Access Key: ")
aws_region = input("Enter your AWS region (default: eu-north-1): ")

# Initialize the AWS client using the provided credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Specify your AWS region
region = 'us-east-1'  # Change this to your desired region

# Create an S3 client
s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# List S3 buckets
try:
    response = s3.list_buckets()
    buckets = response['Buckets']

    print("List of S3 buckets:")
    for bucket in buckets:
        print(bucket['Name'])
except Exception as e:
    print(f"Error listing S3 buckets: {e}")
