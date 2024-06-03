import pytest

@pytest.mark.smoke
def test_addition_f1():
    var1 =10
    var2 = 20
    assert var1+var2 == 30

@pytest.mark.smoke
def substraction_f1():
    val1 = 30
    val2 = 10
    assert val1-val2 == 20
@pytest.mark.sanity
def test_substraction_f1():
    val1 = 30
    val2 = 10
    assert val1-val2 == 20
@pytest.mark.regression
def test_mul_f1():
    var1 = 5
    var2 = 4
    assert var1*var2 == 20

