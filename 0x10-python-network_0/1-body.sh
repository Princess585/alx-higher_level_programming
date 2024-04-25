#!/bin/bash

# Check if a URL was passed as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Assign the URL to a variable
URL="$1"

# Use curl to send a GET request and get the HTTP status code and response body
response=$(curl -s -w "\n%{http_code}" "$URL")

# Split the response to separate the body and the HTTP status code
body=$(echo "$response" | head -n -1)
status_code=$(echo "$response" | tail -n 1)

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
  # Display the response body
  echo "Response body:"
  echo "$body"
else
  echo "Error: Received HTTP status code $status_code"
fi

