# 1). Write a  Python Program To Get The Current Working Directory.
import os
def current_working_directory():
    current_dir = os.getcwd()
    return current_dir # E:\python_selenium\venv\Scripts\python.exe E:\python_selenium\GTM_PS_Batch03\Kiran\selenium\selenium_program.py



# 2). Write a Python Program To Get The Environment Variable
val = os.getenv("br2")
print(val)
chrome_path = os.getenv("CHROME_PATH")
print("chrmepath :", chrome_path)


# 3). Write a Python Program To Set The Environment Variable

def set_env_variable(var_name, var_value):
    os.environ[var_name] = var_value
    print(f"Environment variable {var_name} set to {var_value}")
set_env_variable("kiran", "global")

