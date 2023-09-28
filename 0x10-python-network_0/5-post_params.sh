#!/bin/bash
#this script sends a post request to an endpoint using curl while setting the
#body using variables
URL="$1"
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

curl -X POST -d "email=$EMAIL&subject=$SUBJECT" -s "$URL"
