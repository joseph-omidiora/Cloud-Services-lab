#Language: Python 3
#import libraries
import boto3
import os

# Prompt the user for AWS access key and secret key
aws_access_key_id = os.environ['aws_access_key_id'] 
aws_secret_access_key = os.environ['aws_secret_access_key']

# Specify your AWS region
aws_region = ['eu-west-1'] 

# Initialize the AWS client using the provided credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Specify your S3 bucket name
bucket_prefix = 'mj-accesslog'  # this is to make all buckets created universally unique

for region in aws_region:
    # Create an S3 client for the current region
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    bucket_name = f"{bucket_prefix}-{region}"

    # Create an S3 bucket with appropriate location constraint
    try:
        if region == 'eu-north-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"S3 bucket created successfully: {bucket_name}")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")