#!/bin/sh  

# execute the pipeline
echo "Execute the pipeline"
python /Users/chitraahuja/Desktop/2023-amse-template/data/script.py

# test if pipeline works correct
echo "Test if pipeline works correctly"
pytest /Users/chitraahuja/Desktop/2023-amse-template/data/script_test.py