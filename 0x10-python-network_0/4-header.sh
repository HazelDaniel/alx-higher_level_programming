#!/bin/bash
#a script that sends a get request to and endpoint with an header variable
curl -sH "X-School-User-Id: 98" "${1}"
