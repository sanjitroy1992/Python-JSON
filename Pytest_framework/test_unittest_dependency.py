"""
In this unit test we have defined the following levels:
1. class level suite setup and teardown
2. test level suite setup and teardown
3. tests

** In order to run tests in a dependency order we need to use pytest-dependency pypi module
Install with: pip install pytest-dependency

setps:
1. import pytest
2. First example shows how to use using test methods. use fixture like @pytest.mark.dependency(['testcase_name'])
3. Second example shows how to use using class methods. use fixture like @pytest.mark.dependency(['TestClass::test_a'])
4. this way we can dependent order the tests
5. pytest-ordering usage documentation: https://pytest-dependency.readthedocs.io/en/stable/usage.html

command to execute the tests: pytest test_unittest_dependency.py -v -s -rsx
-v: verbose
-s: print statement
-rsx: to report failure message
"""
import unittest
import pytest

## Example 1
@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False

@pytest.mark.dependency()
def test_b():
    pass

@pytest.mark.dependency(depends=["test_a"])
def test_c():
    pass

@pytest.mark.dependency(depends=["test_b"])
def test_d():
    pass

@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    pass

## Example 2
class TestClass(object):

    @pytest.mark.dependency()
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency()
    def test_b(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b", "TestClass::test_c"])
    def test_e(self):
        pass

if __name__ == '__main__':
    unittest.main()