def greeting():
    print("Welcome to Python Programming")


# greeting()
# greeting()
# greeting()
# greeting()

def greeting_new(msg):
    print(msg)

# greeting_new("Good Morning")
# greeting_new("Good Evening")
# greeting_new("Welcome")


def addition(param1, param2):
    print("value of param1 :", param1)
    print("value of param2 :", param2)
    print("addition of param :", param1+param2)


# pass by value
addition(40, 50)

print("_"*50)
# pass by reference
x = 500
y = 800
addition(x, y)

print("_"*50)
# change the param sequence to call
addition(param2=x, param1=y)

# Home-work:
# write a python program for simple calculator and perform math operations like
# addition
# multiplication
# subtraction
# division
# with help of function

# Passing the default value to function parameter
# Rules
# -> if param has default value then no need to pass value for default param while calling the function
# - User can overwrite the default param value while calling the function.
# - Default parameters always set on right of all param,
# - Default parameter should always follow the non default parameters.
def addition_value(num1, num2, num3=40):
    print("addition :", num1 + num2 + num3)

print("_"*50)
addition_value(30, 50)
addition_value(30, 50, 60)

# Set param data type

def multiplication_value(num1 : int, num2: int):
    print("multiplication output:", num1*num2)

print("_"*50)
multiplication_value("Hello", 3)
# multiplication_value("Hello", "Python")  # can't multiply sequence by non-int of type 'str'
multiplication_value(10, 3)

#########################
# *args argument of function.

# -> *args should always come at the end of the param list.
# *args : accepts n number of values and consider tuple of values

def function3(*args, x, y):
    print("value of x :", x)
    print("value of y :", y)
    print(args)
    for val in args:
        print(val)

print("_"*30)
#function3(4, 7, 2, 8, 12, 'Hello', 100, 200) # function3() missing 2 required keyword-only arguments: 'x' and 'y'
function3(4, 7, 2, 8, [3, 6, 7], 'Hello', x=100, y=200)


###############
# **kwargs : This accepts the param values in key value formate
# default structure is dictionary formate to get all the values

def user_info(**kwargs):
    print(kwargs)
    for key, val in kwargs.items():
        print(key,":", val)


user_info(name='John', email='john@gmail.com', phone=54353543, address='Mumbai')

def user_info_details(param1, *args, **kwargs):
    print("param1 :", param1)
    print("args :", *args)
    print(kwargs)
    for key, val in kwargs.items():
        print(key,":", val)

print("_"*50)
user_info_details(100, 3,4 ,5, 6, user_id='user005', city='Bangalore', country='India', state='Karnataka')

def login(**kwargs):
    db_username = 'user12'
    db_password = 'User@123'

    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Access Denied")


print("_"*50)
login(username='user12', password='User@123')  # Login Successful
login(username='user12', password='User@1234') # Access Denied


########################
# get return value from the function

def calculation(num1, num2, num3):
    return num1+num2+num3

result = calculation(40, 50, 60)
print("result :", result)

def mul_add(n1, n2, n3, m1):
    result = calculation(n1, n2, n3)
    print("multiplication :", result*m1)
    return result*m1


print("_"*50)
mul_result = mul_add(1, 2, 3, 4)
print("Mul result :", mul_result)


def multi_ops(n1, n2):
    return n1+n2, n1*n2, n1-n2
    # print("Hello") : code is not reachable
print("_"*50)


results = multi_ops(50, 40)
print("result :", results)

add, mul, sub = multi_ops(100, 50)
print("addition :", add)
print("multiplicaiton :", mul)
print("subtraction :", sub)

# list1 = [5, 6, 7, 8]
#
# max(list)

################# Function documentation ##########
def factorials(num1):
    """
    This function will get the factorials of any given number and return it
    :param num1: this is required input number
    :return: int
    """
    fact = 1
    for i in range(num1, 0, -1):
        fact = fact*i

    return fact

print(factorials(5))

print(factorials.__doc__)
"""
This function will get the factorials of any given number and return it
    :param num1: this is required input number
    :return: int

"""
help(factorials)

"""
Help on function factorials in module __main__:

factorials(num1)
    This function will get the factorials of any given number and return it
    :param num1: this is required input number
    :return: int

"""

print("_"*50)
################### Function recursion ###########

temp = 1
def fun1():
    global temp
    print(temp)
    temp = temp+ 1
    if temp == 10:
        exit()
    fun1()

# RecursionError: maximum recursion depth exceeded
#fun1()


# get factorials of all the numbers between 1 to 10

print("_"*50)
def fact_value(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact*i

    print(f"fact of {n}:", fact)
    n = n - 1
    if n == 0:
        exit()
    fact_value(n)


fact_value(10)
