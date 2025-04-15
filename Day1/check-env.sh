#!/bin/bash

if [ "${ENV}" != "prod" ]; then
    echo "ENV is not set to prod"
    exit 1
else
    echo "ENV is set to prod"

fi
