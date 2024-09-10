import pytest

@pytest.mark.dependency(depends=["test_pqr"])
@pytest.mark.order(1)
def test_abc():
    var1 = 10
    var2 = 20
    assert var1 + var2 == 40
    print("test addition successful")


@pytest.mark.dependency(depends=["test_pqr"])
@pytest.mark.order(2)
def test_xyz():
    var1 = 10
    var2 = 20
    assert var1 * var2 == 200
    print("test multiplication successful")


@pytest.mark.dependency
@pytest.mark.order(3)
def test_pqr():
    var1 = 10
    var2 = 200
    assert var2 - var1 == 300
    print("test subtraction successful")
