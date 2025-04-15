#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Enter the EC2 instance type in input"
    exit 1
fi

ec2_type=$1

result="The EC2 instance type is '${ec2_type}'"
echo $result
