import pytest


@pytest.mark.parametrize("user,password",[("abc","123"),("cdb","235"),("cgh","398")])
def test_name(user,password):
    print(user,"--",password)
    print(user+"--"+password)
    print("Kiran")