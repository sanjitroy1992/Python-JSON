"""
setps:
1. import pytest
2. under test section user @pytest.mark.parametrize("arguments", test_data )
3. test_data: Could be in nested or list format

command to execute the tests: pytest test_parametrize.py -v -s
-v: verbose
-s: print statement
"""

import pytest

test_data1 = [[1,2,3], [2,3,5], [4,5,9]]
test_data2 = [[1,2,3], [2,3,5], [4,5,10]]

@pytest.mark.parametrize("a,b,c",test_data1)
def test_with_params1(a,b,c):
    assert a+b == c

@pytest.mark.parametrize("a,b,c",test_data2)
def test_with_params2(a, b, c):
    assert a+b == c
