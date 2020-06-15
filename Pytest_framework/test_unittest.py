"""
In this unit test we have defined the following levels:
1. class level suite setup and teardown
2. test level suite setup and teardown
3. tests
command to execute the tests:
pytest test_unittest.py -v -s

-v: verbose
-s: print statement
"""
import unittest

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

    def test1(self):
        print("This is unittest test1")

    def test2(self):
        print("This is unittest test2")

    def test3(self):
        print("This is unittest test3")

    def test4(self):
        print("This is unittest test4")

if __name__ == '__main__':
    unittest.main()