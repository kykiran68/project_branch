"""
# install pytest library, then create test file with test_ as prefix and add test function
python -m pytest -v .\test_smoke_cases.py
"""
import pytest


@pytest.fixture(scope='function')
def setup():
    print("Execution initiated \n")
    yield
    print("\n Execution completed \n")


def test_addition(setup):
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
    print("test addition successful")


def test_multiplication(setup):
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")



def test_subtraction(setup):
    var1 = 10
    var2 = 200
    assert var2 - var1 == 300
    print("test subtraction successful")


def division():
    var1 = 10
    var2 = 20
    assert var1 // var2 == 30
