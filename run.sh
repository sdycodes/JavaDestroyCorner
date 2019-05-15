#!/bin/bash
python3 gen.py
rm ./tests/.DS_Store
./run_without_gen.sh
