#!/bin/bash
# a script that prints out all the methods that the server accepts
curl -X OPTIONS -i "$1"
