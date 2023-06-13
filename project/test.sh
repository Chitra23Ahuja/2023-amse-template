#!/bin/sh  

# execute the pipeline
echo "Execute the pipeline"
python ./data/script.py

# test if pipeline works correct
echo "Test if pipeline works correctly"
pytest ./data/script_test.py

