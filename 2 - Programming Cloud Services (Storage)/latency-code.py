import boto3
import time
import matplotlib.pyplot as plt
import os

# AWS credentials
# Prompt the user for AWS access key and secret key
aws_access_key_id = os.environ['aws_access_key_id'] 
aws_secret_access_key = os.environ['aws_secret_access_key']

# S3 regions and bucket names
regions = ['us-east-1', 'us-west-2', 'eu-west-1']
bucket_names = ['buc-mj-us-east-1',  'buc-mj-us-west-2','buc-mj-eu-west-1']

# Object sizes in MB
object_sizes = [1, 10, 100, 500]

def upload_object(s3, bucket, key, data):
    start_time = time.time()
    s3.put_object(Bucket=bucket, Key=key, Body=data)
    end_time = time.time()
    return end_time - start_time

def download_object(s3, bucket, key):
    start_time = time.time()
    s3.get_object(Bucket=bucket, Key=key)
    end_time = time.time()
    return end_time - start_time

def main():
    latencies = {'Upload': {size: [] for size in object_sizes},
                 'Download': {size: [] for size in object_sizes}}

    for region, bucket_name in zip(regions, bucket_names):
        s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

        for size in object_sizes:
            data = b'0' * (size * 1024 * 1024)  # Creating data of specified size in MB

            upload_latency = upload_object(s3, bucket_name, f'{size}MB_object', data)
            download_latency = download_object(s3, bucket_name, f'{size}MB_object')

            latencies['Upload'][size].append(upload_latency)
            latencies['Download'][size].append(download_latency)

    # Plotting results
    for operation in ['Upload', 'Download']:
        for size in object_sizes:
            plt.plot(regions, latencies[operation][size], label=f'{size}MB')

        plt.title(f'{operation} Latency Across Regions')
        plt.xlabel('Regions')
        plt.ylabel('Latency (seconds)')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()
