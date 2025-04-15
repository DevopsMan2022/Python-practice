#!/bin/bash

if [ $# -ne 1 ]; then
    echo "please Enter the valid  directory path name"
    exit 1
fi

directory_path=$1

if [ -d "${directory_path}" ]; then
    echo "directory "${directory_path}" already exists"
else
    mkdir -p "${directory_path}"
fi
