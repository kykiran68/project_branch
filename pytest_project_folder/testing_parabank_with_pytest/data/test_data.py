# parabank_testing_with_pytest/data/test_data.py
from datetime import datetime

# URL for the website
url = "https://parabank.parasoft.com/parabank/index.htm"

# Valid credentials
VALID_USERNAME = "john"
VALID_PASSWORD = "demo"

# Invalid credentials
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "invalid_pass"

# Registration data
now = datetime.now()
REGISTRATION_DATA = [
    ("Joh", "Do", "123 Elm S", "Some Cit", "CAh", "90001", "555-555-5555", "123-45-6789", VALID_USERNAME+"@#$"+str(now), VALID_PASSWORD,VALID_PASSWORD),
    ("Joh", "De", "123 Elm St", "Some City", "CA", "90001", "555-555-5555", "123-45-6789", INVALID_USERNAME, "short", "long")
]

# Fund transfer data
TRANSFER_DATA = [
    ("12345", "54321", "100", True),
    ("12345", "54321", "#$%", False)  # Edge case with zero amount
]

# Bill pay data
BILL_PAY_DATA = [
    ("Some Payee", "100", True),
    ("Invalid Payee", "0", False)  # Edge case with zero amount
]
