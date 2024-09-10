def exception_function():
    try:
        num1 = 40
        num2 = "Hello"

        addition = num1 + num2
        print("Addition :", addition)
    except Exception as e:
        print(e)
        print("Addition of integer and string is not allowed")

    print("_"*50)

    print("Execution successful")


#exception_function()

# Explicit raise exception
def explicit_exception_function():
    try:
        num1 = 40
        num2 = "Hello"

        addition = num1 + num2
        print("Addition :", addition)
    except Exception as e:
        print(e)
        print("Addition of integer and string is not allowed")
        raise

    print("_"*50)

    print("Execution successful")

#explicit_exception_function()

# try - except - else
def try_except_else(x, y):
    try :
        num1 = x
        num2 = y
        print("Division :", num1//num2)

    except Exception as e:
        print(e)
        print("division by zero is not valid operation")
    else:
        # This else part will only execute if there is no exception
        print("division operation is successful")


#try_except_else(40, 5)
#try_except_else(40, 0)

# try - except - else - finally
# finally : Finally section code always going to execute if whether there is exception or no exception.

def try_except_else_finally(x, y, z):
    try :
        num1 = x
        num2 = y
        print("Division :", num1//num2)

    except Exception as e:
        print(e)
        print("division by zero is not valid operation")
    else:
        # This else part will only execute if there is no exception
        print("division operation is successful")
    finally:
        for i in range(1, 11):
            print(i, "*", z, ":", i*z)

#try_except_else_finally(45, 3, 5)
#print("_"*50)
#try_except_else_finally(45, 0, 5)


# Handle multiple exception
def handle_multiple_exception(num1, num2, num3):
    try:
        addition = num1 + num2
        print("addition  :", addition)

        multiplication = num1 * num2
        print("multiplication :", multiplication)

        division = num1 // num2
        print("division :", division)

        assert num1 == num2
    except TypeError:
        print("Addition of integer and string is not allowed")
    except ZeroDivisionError:
        print("Division of number with zero is not allowed")
    except AssertionError:
        print("Both numbers are not equal")
    except Exception as e:
        raise


#handle_multiple_exception(50, 22, 30)

# Nested exception Handling
def nested_exception_handling(num1, num2):
    try:
        addition = num1 + num2
        print("addition:", addition)
        try:
            division = num1//num2
            print("division :", division)
        except Exception as e:
            #print(e)
            print("Divide by zero is not allowed")

    except Exception as e:
        print(e)
        print("Both the values should be integer")


#nested_exception_handling(30, 2)
#nested_exception_handling(30, 'Hello')
#nested_exception_handling(15, 0)

############ custom exception #############
class CustomError(Exception):
    """This is custom exception class"""
    def __init__(self):
        print("Raising the custom exception with condition")

def raise_custom_exception():
    for i in range(20):
        if i == 14:
            raise CustomError()
        else:
            print(i)


#raise_custom_exception()


# List of all possible errors and exceptions
"""
ArithmeticError
OverflowError
ZeroDivisionError
FloatingPointError
BufferError
LookupError
AssertionError
AttributeError
 EOFError
GeneratorExit
 ImportError
ModuleNotFoundError
 IndexError
KeyError
MemoryError
NameError
NotImplementedError
OSError(
RecursionError
ReferenceError
RuntimeError
StopIteration
 SyntaxError
SystemError
SystemExit
TypeError
UnboundLocalError
UnicodeError
ValueError
"""
