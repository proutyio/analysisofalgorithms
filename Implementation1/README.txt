CS 325 - Implementation 1

Closest Pair of Points - Winter 2017
Group project by Kyle Prouty, Levi Willmeth, and Andrew Morrill.

-------------------------------------------------------------------------------

Compiling and running instructions:

We wrote our algorithms in Python 2.x which is the default on most machines.

-------------------------------------------------------------------------------

You can run any of the BruteForce, DivideConquer, or EnhancedDivideConquer
programs from the command line like this:
$ python BruteForce.py [inputfile]
Example:
$ python BruteForce.py points.10000.int.input

You can also redirect the output to a file if you prefer:
$ python BruteForce.py points.10000.int.input > output_bruteforce.txt

-------------------------------------------------------------------------------

We also included a Bash script to run all 3 algorithms using the same input
file.  This script measures the total runtime for each algorithm, including
the initial sorts and writing outputs to a file.  It also automatically creates
3 output files, output_BruteForce.txt, output_DivideConquer.txt, etc.
$ ./runScripts.sh [inputfile]
Example:
$ ./runScripts.sh example.input
If you do not specify an input file, it will default to using example.input
