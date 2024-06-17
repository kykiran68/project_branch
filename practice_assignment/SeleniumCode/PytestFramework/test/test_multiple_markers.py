import pytest

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.m3
@pytest.mark.m1
@pytest.mark.order(3)
def test_addition_file1():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 30
    print("test addition successful")


@pytest.mark.sanity
@pytest.mark.m2
@pytest.mark.order(2)
def test_multiplication_file1():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")


@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.m1
@pytest.mark.order(1)
def test_subtraction_file1():
    var1 = 10
    var2 = 200
    assert var2 - var1 == 300
    print("test subtraction successful")
