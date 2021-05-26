#!/bin/bash

# This script downloads the first asset from the latest Github release of a
# private repo.
#
# PREREQUISITES
#
# curl, jq
#
# USAGE
#
# Set owner and repo variables inside the script, make sure you chmod +x it.
#
#     ./download.sh "--GITHUB TOKEN HERE--"
#

# Define variables
echo "---------------------------------------------------------------------"
echo "Define variables"
echo "---------------------------------------------------------------------"

owner="devoli170"
repo="home_pv"
GITHUB_API_TOKEN=$1
GH_API="https://api.github.com"
GH_REPO="$GH_API/repos/$owner/$repo"
GH_LATEST="$GH_REPO/releases/latest"
AUTH="Authorization: token $GITHUB_API_TOKEN"

# Read asset name and id
echo "---------------------------------------------------------------------"
echo "Read asset name and id"
echo "---------------------------------------------------------------------"

response=$(curl -sH "$AUTH" $GH_LATEST)
id=`echo "$response" | jq '.assets[0] .id' |  tr -d '"'`
