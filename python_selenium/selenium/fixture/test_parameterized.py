import pytest

@pytest.mark.smoke

def test_addition_fil2():
    var1 =10
    var2 = 20
    assert var1+var2 == 30

@pytest.mark.sanity
def substraction_fil2():
    val1 = 30
    val2 = 10
    assert val1-val2 == 20

@pytest.mark.sanity
@pytest.mark.xfail
def test_substraction_fil2():
    val1 = 30
    val2 = 10
    assert val1-val2 == 20

@pytest.mark.regression
@pytest.mark.xfail
def test_mul_fil2():
    var1 = 5
    var2 = 4
    assert var1*var2 == 300

@pytest.mark.monkey
@pytest.mark.skip
def test_div_fil2():
    var_1 = 20
    var2 = 2
    assert var_1/var2==10
