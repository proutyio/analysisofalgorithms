#!/bin/sh

start=$(date +%s%6N)
python BruteForce.py $1 > output_BruteForce.txt
end=$(date +%s%6N)
echo "BruteForce ran $1 in `expr $end - $start` microseconds."

start=$(date +%s%6N)
python DivideConquer.py $1 > output_DivideConquer.txt
end=$(date +%s%6N)
echo "DivideConquer ran $1 in `expr $end - $start` microseconds."

start=$(date +%s%6N)
python EnhancedDivideConquer.py $1 > output_EnhancedDivideConquer.txt
end=$(date +%s%6N)
echo "EnhancedDivideConquer ran $1 in `expr $end - $start` microseconds."
