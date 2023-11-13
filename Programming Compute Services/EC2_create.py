#Language: Python 3
import boto3

# Prompt the user for AWS access key and secret key
aws_access_key_id = input("Enter your AWS Access Key ID: ")
aws_secret_access_key = input("Enter your AWS Secret Access Key: ")

aws_region = input("Enter your AWS region (default: eu-north-1)")

# Initialize the AWS client using the provided credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=aws_region,
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Define the instance parameters
instance_type = 't3.micro'
ami_id = 'ami-03a2c69daedb78c95'  # Replace with your desired AMI ID
key_name = 'mj-key'  # Replace with your SSH key pair name

# Launch the EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1
)

# Extract the instance ID from the response
instance_id = response['Instances'][0]['InstanceId']

# Wait for the instance to be running
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Get information about the running instance
response = ec2.describe_instances(InstanceIds=[instance_id])
instance = response['Reservations'][0]['Instances'][0]

# Print the instance details
print(f"Instance ID: {instance_id}")
print(f"Public DNS: {instance['PublicDnsName']}")
print(f"Private IP: {instance['PrivateIpAddress']}")
