#! /bin/bash

find . -name "__pycache__" -exec rm -rf "{}" \;
find . -name "*.pyc" -exec rm -f "{}" \;