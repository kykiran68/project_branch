"""
Fixture scope:

function scope = function level fixture will execute for each of the test function in the file.
module scope = module level fixture will execute once for each module file
package scope = package level fixture will execute for each of the folder which contains module files.
session scope = session level fixture has wider scope which will initiate with session of automation execution
class scope = class level fixture will execute for specific class only.

"""
import pytest

@pytest.mark.smoke
def test_addition_file3():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
    print("test addition successful")


@pytest.mark.sanity
def test_multiplication_file3():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")


@pytest.mark.regression
def test_subtraction_file3():
    var1 = 10
    var2 = 200
    assert var2 - var1 == 300
    print("test subtraction successful")
