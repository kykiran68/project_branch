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






