#!/bin/bash
set -e

# Stop the running container (if any)
echo "Hi"
c=`docker ps | awk -F " " '{print $1}'`
docker rm -f $c
