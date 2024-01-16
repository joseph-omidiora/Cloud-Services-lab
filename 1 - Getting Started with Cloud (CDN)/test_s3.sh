#!/bin/bash

# S3 Bucket URL and resource path
s3_bucket_url="https://lab1-mj.s3.amazonaws.com/"
resource_path="index.html"

# CSV file header
echo "HTTP Code,Time" > s3_test_results.csv

# Loop for 30 tests
for ((i=1; i<=30; i++)); do
    # Build the curl command
    curl_command="curl -s -w '%{http_code},%{time_total}\n' -o /dev/null $s3_bucket_url$resource_path"

    # Execute the curl command and append the result to the CSV file
    eval $curl_command >> s3_test_results.csv

    # Add a sleep interval between requests (optional)
    sleep 2
done

echo "Test completed. Results saved to s3_test_results.csv"
