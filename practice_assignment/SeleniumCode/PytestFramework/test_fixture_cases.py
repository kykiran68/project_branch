"""
Fixture scope:

function scope = function level fixture will execute for each of the test function in the file.
module scope = module level fixture will execute once for each module file
package scope = package level fixture will execute for each of the folder which contains module files.
session scope = session level fixture has wider scope which will initiate with session of automation execution
class scope = class level fixture will execute for specific class only.

"""
import pytest


@pytest.fixture(scope='function', autouse=True)
def setup():
    print("function Execution initiated \n")
    yield
    print("\n function Execution completed \n")


@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print("Module Execution initiated \n")
    yield
    print("\n Module Execution completed \n")


@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print("Session Execution initiated \n")
    yield
    print("\n Session Execution completed \n")


@pytest.fixture(scope='package', autouse=True)
def setup_package():
    print("Package Execution initiated \n")
    yield
    print("\n Package Execution completed \n")


def test_addition():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
    print("test addition successful")


def test_multiplication():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")


def test_subtraction():
    var1 = 10
    var2 = 200
    assert var2 - var1 == 300
    print("test subtraction successful")


def division():
    var1 = 10
    var2 = 20
    assert var1 // var2 == 30
