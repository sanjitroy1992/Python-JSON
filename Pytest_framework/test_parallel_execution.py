"""
** In order to run tests in parallel
Install with: pip install pytest-xdist

setps:
1. Write tests

command to execute the tests: pytest -n 4 test_parallel_execution.py -v -s
-v: verbose
-s: print statement
-n: number of parallel processes

"""
import time

def test1():
    time.sleep(3)

def test2():
    time.sleep(3)

def test3():
    time.sleep(2)

def test4():
    time.sleep(2)