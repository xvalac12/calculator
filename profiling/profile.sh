#!/bin/bash

#Has to be run from inside profiling folder

echo "Running profiling on 10 input numbers" > vystup.out
seq 1000 1000000 | shuf | head -10 | python3 -m cProfile -s tottime ../src/profiling.py >> vystup.out

echo "Running profiling on 100 input numbers" >> vystup.out
seq 1000 1000000 | shuf | head -100 | python3 -m cProfile -s tottime ../src/profiling.py >> vystup.out

echo "Running profiling on 1000 input numbers" >> vystup.out
seq 1000 1000000 | shuf | head -1000 | python3 -m cProfile -s tottime ../src/profiling.py >> vystup.out

echo "Running profiling on 1000 000 input numbers" >> vystup.out
seq 1000 10000000 | shuf | head -1000000 | python3 -m cProfile -s tottime ../src/profiling.py >> vystup.out
