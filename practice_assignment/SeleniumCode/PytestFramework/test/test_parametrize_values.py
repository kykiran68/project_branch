import pytest
from test_data import *
env = 'Prod'


@pytest.mark.parametrize("username, password", [
    ('testuser1', 'P@assword'),  ('testuser2', 'Admin@1234'), ('testuser3', 'User@123')
])
def test_login(username, password):
    db_username = 'testuser3'
    db_password = 'User@123'
    assert username == db_username and password == db_password, "Invalid credentials"
    print("Login Successful")


@pytest.mark.parametrize("greeting", greetings_msg)
def test_greeting(greeting):
    assert greeting

