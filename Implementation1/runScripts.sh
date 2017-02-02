#!/bin/sh

start=$(date +%s%6N)
python BruteForce.py $1 > output_BruteForce.txt
end=$(date +%s%6N)
echo "BruteForce ran $1 in `expr $end - $start` ms."

echo "Starting DivideConquer.py"
start=$(date +%s%6N)
python DivideConquer.py $1 > output_divideConquer.txt
end=$(date +%s%6N)
echo "DivideConquer ran $1 in `expr $end - $start` ms."

echo "Starting DivideConquerEnhanced.py"
start=$(date +%s%6N)
python DivideConquerEnhanced.py $1 > output_divideConquerEnhanced.txt
end=$(date +%s%6N)
echo "DivideConquerEnhanced ran $1 in `expr $end - $start` ms."
