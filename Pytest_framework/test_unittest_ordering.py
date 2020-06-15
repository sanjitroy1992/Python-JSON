"""
In this unit test we have defined the following levels:
1. class level suite setup and teardown
2. test level suite setup and teardown
3. tests

** In order to run tests in a particular order we need to use pytest-ordering pypi module
Install with: pip install pytest-ordering

setps:
1. import pytest
2. under test section user @pytest.mark.run(order=1)
3. this way we can order the tests
4. pytest-ordering usage documentation: https://pytest-ordering.readthedocs.io/en/develop/#:~:text=pytest-ordering

command to execute the tests: pytest test_unittest_ordering.py -v -s
-v: verbose
-s: print statement
"""
import unittest
import pytest

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is class test setup")

    @classmethod
    def tearDownClass(cls):
        print("This is class tear down")

    def setUp(self):
        print("This is test setup")

    def tearDown(self):
        print("This is test teardown")
    @pytest.mark.run('second')
    def test1(self):
        print("This is unittest test1")

    @pytest.mark.run(order=4)
    def test2(self):
        print("This is unittest test2")

    @pytest.mark.run(order=4)
    def test3(self):
        print("This is unittest test3")

    @pytest.mark.run(order=6)
    def test4(self):
        print("This is unittest test4")

    @pytest.mark.run('last')
    def test5(self):
        print("This is unittest test5")

    @pytest.mark.run('first')
    def test6(self):
        print("This is unittest test6")

if __name__ == '__main__':
    unittest.main()