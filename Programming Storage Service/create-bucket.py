#Language: Python 3
import boto3

# Prompt the user for AWS access key and secret key
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
regions = ['us-east-1', 'us-west-2', 'eu-west-1'] 

# Specify your S3 bucket name
bucket_prefix = 'enilol'  # Change this to a unique name

for region in regions:
    # Create an S3 client for the current region
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    bucket_name = f"{bucket_prefix}-{region}"

    # Create an S3 bucket with appropriate location constraint
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"S3 bucket created successfully: {bucket_name}")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")