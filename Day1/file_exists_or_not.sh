#!/bin/bash

if [ $# -ne 1 ]; then
    echo "please Enter the valid  file name"
    exit 1
fi

file_name=$1

if [ -f "${file_name}" ]; then
    echo "file "${file_name}" exists in the current directory"
else
    echo "file "${file_name}" does not exists in the current directory"

fi
