import pytest


@pytest.fixture(scope='function', autouse=True)
def setup():
    print("function execution begin\n")
    yield
    print(" function Ececution completed \n")

@pytest.fixture(scope='package', autouse=True)
def setup_package():
    print("package execution begin\n")
    yield
    print(" package Ececution completed \n")

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


