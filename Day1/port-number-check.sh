#!/bin/bash

if [ $# -ne 1 ]; then
    echo "please Enter the valid  port number"
    exit 1
fi

port_number=$1

if [ "${port_number}" >= 1024 && "${port_number}" <= 65535 ]; then
    echo "port number "${port_number}" exists in the proper range"
else
    echo "port number "${port_number}" does mot exists in the proper range"

fi
