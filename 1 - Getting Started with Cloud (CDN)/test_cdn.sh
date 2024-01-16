#!/bin/bash

# List of possible locations
locations=("New York" "London" "Tokyo" "Sydney" "Singapore", "Taiwandadfa")

# CDN URL and resource path
cdn_url="https://d1myz74c2xeplk.cloudfront.net/"
resource_path="index.html"

# CSV file header
echo "Location,HTTP Code,Time" > cdn_test_results.csv

# Loop for 30 tests
for ((i=1; i<=30; i++)); do
    # Randomly select a location
    random_location=${locations[$RANDOM % ${#locations[@]}]}

    # Build the curl command with the selected location
    curl_command="curl -s -w '$random_location,%{http_code},%{time_total}\n' -o /dev/null $cdn_url$resource_path"

    # Execute the curl command and append the result to the CSV file
    eval $curl_command >> cdn_test_results.csv

    # Add a sleep interval between requests (optional)
    sleep 2
done

echo "Test completed. Results saved to cdn_test_results.csv"
