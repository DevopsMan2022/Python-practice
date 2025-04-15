#!/bin/bash

if [ $# != 2 ]; then
    echo "provide 2 numbers to compare"
    exit 1
fi

num1=$1
num2=$2

if [ "${num1}" -eq "${num2}" ]; then
    echo ""${num1}" and "${num2}" are equal"
    exit 1
fi

if [ "${num1}" -gt "${num2}" ]; then
    echo ""${num1}""
    exit 1
else
    echo ""${num2}""
fi