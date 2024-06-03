def greeting():
    print("welcome")
greeting()

# 2
def addition(para1,para2):
    print("addition of parameter1 and parameter2 is : ",para1+para2)

# pass by value
addition(40,50)

# pass by reference
x =30
y =80
addition(x,y)

# change parameter sequence to call
addition(para2 =x , para1 = y )




# calculator program



def calculator(para3,para4):
    print("Please select your operation : \n1 Addition \n2 substraction \n3 division \n4 multiplication ")
    num1 = int(input("Enter output : "))

    if num1==1:
        sum = para3+para4
        print(sum)
    elif num1==2:
        sub = para3-para4
        print(sub)
    elif num1==3:
        div = para3/para4
        print(div)
    elif num1==4:
        multi = para3*para4
        print(multi)
    else:
        print("Invalid Input!!")
num1 = int(input("Enter first no. : "))
num2 = int(input("Enter second no : "))
calculator(num1,num2)




'''



def substraction(n1,n2):
    return n1-n2
def division(n1,n2):
    return n1/n2
def multiplication(n1,n2):
    return n1*n2
def addition(n1,n2):
    return n1+n2

print("Please select your operation : \n1 Addition \n2 substraction \n3 division \n4 multiplication ")
operation = int(input("select input : "))
num1 = int(input("Enter first no. : "))
num2 = int(input("Enter second no : "))
if operation==1:
    print(num1, "+", num2 ,"=", addition(num1,num2))
elif operation == 2:
    print(num1, "-", num2, "=", substraction(num1, num2))
elif operation==3:
    print(num1, "/", num2, "=", division(num1, num2))
elif operation==4:
    print(num1, "*", num2, "=", multiplication(num1, num2))
else:
    print("Invalid Input!!")

'''
"""
global variable : The variable that can access by every function of the module.
local variable : The variable which we declare on function level and can be access inside the function.
                scope is limited to function
non-local variable: The variable we declare in the outer function and it is available to access all the
               inner functions, then it is known as non local variable.

"""
# global variable
var_p = 500


def function1():
    print("________function1_________")
    global var_p
    var_q = 300  # local variable
    var_p = 400
    print("global variable value var_p :", var_p)
    print("local variable value var_q :", var_q)


def function2():
    var_r = 200  # local variable
    print("________function2_________")
    print("global variable value var_p :", var_p)
    print("local variable value var_r :", var_r)


function2()
function1()
function2()

print("_"*50)
##########################

var_x = 600 # global

def outer_function():
    var_y = 700 # non-local

    def inner_fun1():
        print("----------Inner Function1---------")
        global var_x
        nonlocal var_y
        var_z = 800 # local variable
        var_y = 1100
        var_x = 1200
        print("global varx :", var_x)
        print("non local vary :", var_y)
        print("local varz :", var_z)

    def inner_fun2():
        print("----------Inner Function2---------")
        var_w = 900 # local variable
        print("global varx :", var_x)
        print("non local vary :", var_y)
        print("local varw :", var_w)

    inner_fun1()
    inner_fun2()

outer_function()