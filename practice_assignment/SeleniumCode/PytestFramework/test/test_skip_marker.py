"""
Fixture scope:

function scope = function level fixture will execute for each of the test function in the file.
module scope = module level fixture will execute once for each module file
package scope = package level fixture will execute for each of the folder which contains module files.
session scope = session level fixture has wider scope which will initiate with session of automation execution
class scope = class level fixture will execute for specific class only.

"""
import pytest

env = 'Prod'

@pytest.mark.skip
@pytest.mark.smoke
def test_addition_file3():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
    print("test addition successful")


@pytest.mark.sanity
@pytest.mark.skipif(env == 'Prod', reason="Can not execute on product env")
def test_multiplication_file3():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")


@pytest.mark.regression
def test_subtraction_file3():
    var1 = 10
    var2 = 200
    assert var2 - var1 == 190
    print("test subtraction successful")


# we use the xfail marker, when the test cases are flaky
# if test case pass, then result will show xpassed, if failed then result will show xfailed.
@pytest.mark.regression
@pytest.mark.xfail
def test_add_first_10():
    sum = 0
    for i in range(1, 11):
        sum += i
    assert  sum > 20

@pytest.mark.regression
@pytest.mark.xfail
def test_product_values():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum == 50

def test_product_values1():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum == 50

def test_product_values2():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50

def test_product_values3():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50


def test_product_values_4():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50

def test_product_values_5():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50

def test_product_values_6():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50

def test_product_values_7():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50


def test_product_values_8():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50

def test_product_values_9():
    sum = 0
    for i in range(1, 11):
        sum = sum * i
    assert sum >= 50




