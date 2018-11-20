#!/bin/bash
export LD_PRELOAD=./limit_visible_cpus.so
export OMP_NUM_THREADS=13
python get_ncpus.py
