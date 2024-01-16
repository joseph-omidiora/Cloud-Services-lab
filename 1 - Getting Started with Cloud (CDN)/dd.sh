#!/bin/bash

#url="https://d1myz74c2xeplk.cloudfront.net/"
url="https://lab1-mj-2.s3.eu-west-2.amazonaws.com/index.html"
num_requests=20
output_file="latency_metrics.txt"

echo "Request,Total Time,Connection Time,TTFB" > $output_file

for ((i=1; i<=$num_requests; i++)); do
  result=$(curl -w "$i,%{time_total},%{time_connect},%{time_starttransfer}\n" -o /dev/null -s $url)
  echo -e $result >> $output_file
done
