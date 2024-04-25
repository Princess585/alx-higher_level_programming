#!/bin/bash

# Check if URL is passed as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
URL="$1"

# Use curl to get the response body, and use wc to count the number of bytes
# -s suppresses progress information and errors
# -o sends the output to stdout
# -L follows redirects
# wc -c counts the number of bytes
BODY_SIZE=$(curl -s -L -o - "$URL" | wc -c)

# Display the size of the response body
echo "The size of the response body from '$URL' is $BODY_SIZE bytes."
