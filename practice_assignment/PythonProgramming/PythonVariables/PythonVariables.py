var1 = 10

print(id(var1)) # 140724248464088

var2 = 50
print(id(var2)) # 140724248465368

var3 = 10
print(id(var3)) # 140724248464088

# - If two variable are holding same value, then their memory address is same.
# - Each variable with different value will have their different memory address.

# Rules to defined variable name
# 1. Variable name does not contains space.
#    var 1 = 40 # in valid
#    var_23 = 50 # valid
#    var567 = 70 # valid

# 2. Variable name can not start by number
# 1var = 50 : invalid
# var2num = 60 : valid

# 3. special characters are not allowed in the variable name
# var$3 = 60  : invalid

# 4. There is no limit to defined variable name
mathematic_var_value_holder = 700
print(mathematic_var_value_holder)

#5. Python is case sensitive language, os variable with different will be considered
#   individually.
Name = 'Ashok'
NAME = 'Rahul'
name = 'Mohit'
print(Name, name, NAME)

########### assign single value to multiple variable ########
a = b = c = 700
print("value a :", a)
print("value b :", b)
print("value c :", c)

##### assign different values to different variables ####

p, q, r = 50, 60, 70
print("value of p:", p)
print("value of q:", q)
print("value of r:", r)

########## Mathematical operation with data #####

"""
+  : plus operator
-  : minus operator
*  : multiplication
/  : division with single slash
// : division with double slash
%  : reminder operator
== : equal to operator
!= : not equal to operator
** : power operator
"""

# +  : plus operator

var1 = 60
var2 = 70
var3 = var1 + var2
print("var3 :", var3)
print("addition :", var1+var2)

# - : subtraction
vara = 500
varb = 200
print("subtraction output :", vara-varb)

# * : multiply of two values
varp = 6
varq = 7
print("multiplication :", varp*varq)

# division of values
var_1 = 12
var_2 = 5
# if we divide the number with single slash, then it will provide output in float.
var_3 = var_1 / var_2
print("division :", var_3) # 2.4

# if we divide the number with double slash, then it will provide output in integer
var_4 = var_1 // var_2
print("division :", var_4) # 2

# % :  reminder operator
var_j = 12
var_k = 5

output = var_j % var_k
print("output :", output)
# output : 2

var_l = 100
var_m = 200
var_n = 100
print(var_l == var_n) # True
print(var_l != var_m) # True
print(var_l == var_m) # False

# ** : power operator
var_g = 7
print("square value :", var_g**2)  # 49
print("cube value :", var_g**3)    # 343
print("4 power value :", var_g**4) # 2401


print("_"*50)
# Solve below equation

# (a+b)^2  =a^2 + b^2 + 2ab
a = 4
b = 7

lhs = (a+b)**2
print("lhs result :", lhs)

rhs = a**2 + b**2 + 2*a*b
print("rhs result:", rhs )





