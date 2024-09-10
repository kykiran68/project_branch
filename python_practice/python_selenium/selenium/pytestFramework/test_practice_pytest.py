import pytest


@pytest.fixture(scope='function', autouse=True)
def setup_function():
    print("function execution begin\n")
    yield
    print(" function Ececution completed \n")

@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print("module execution begin\n")
    yield
    print("module Ececution completed \n")

@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print("session execution begin\n")
    yield
    print("session Ececution completed \n")

def test_addition():
    var1 =10
    var2 = 20
    assert var1+var2 == 30
def substraction():
    val1 = 30
    val2 = 10
    assert val1-val2 == 20
def test_substraction():
    val1 = 30
    val2 = 10
    assert val1-val2 == 20
def test_mul():
    var1 = 5
    var2 = 4
    assert var1*var2 == 30