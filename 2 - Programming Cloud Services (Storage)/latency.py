import boto3
import time
import os


# Specify your AWS credentials
aws_access_key_id = os.environ['aws_access_key_id'] 
aws_secret_access_key = os.environ['aws_secret_access_key']


# Specify the AWS regions where your buckets are located
regions = ['us-east-1', 'us-west-2', 'eu-west-1']  # Change these to your bucket's regions

# Specify the bucket name
bucket_names =['buc-mj-us-east-1','buc-mj-us-west-2','buc-mj-eu-west-1']# Change this to your bucket's name

# Object sizes to test (in bytes)
object_sizes = [1024 * 1024, 10 * 1024 * 1024, 100 * 1024 * 1024, 500 * 1024 * 1024]

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

latency_data = {'Upload': {}, 'Download': {}}

def measure_latency(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    latency = end_time - start_time
    return latency, result

for region in regions:
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    
    latency_data['Upload'][region] = []
    latency_data['Download'][region] = []

    for size in object_sizes:
        # Generate a random object key
        object_key = f"test_object_{size}_{int(time.time())}"

        # Generate random data for the object
        data = bytearray(size)
        
        # Upload object
        for bucket_name  in bucket_names :
            upload_latency, _ = measure_latency(s3.put_object, Bucket=bucket_name, Key=object_key, Body=data)
            latency_data['Upload'][region].append(upload_latency)

            # Download object
            download_latency, _ = measure_latency(s3.get_object, Bucket=bucket_name, Key=object_key)
            latency_data['Download'][region].append(download_latency)


