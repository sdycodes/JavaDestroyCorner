#!/bin/bash
rm -r outputs/
mkdir outputs
rm res.txt
touch res.txt
python3 test.py 
echo "test finish"
python3 compare.py >> res.txt
echo "compare finish"
