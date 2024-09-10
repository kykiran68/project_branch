# 7). Python program to print the square and cube of a given number.
a = 5
print("The square of number is : ", a ** 2 )
print("The cube of number is : ", a ** 3 )
print("*"*50)

# 8). Python program to interchange values between variables.
a=20
b=50
a , b = b , a
print("a :", a)
print("b : ", b)
print("_"*50)

# 9). Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)
base = 3
height = 4
hypo = (base**2 + height**2)**(1/2)
print("The hypotenious of triange is",hypo)
print("*"*50)

# 10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
x = 40
y = 20
z = (x+y)**2
temp = x**2 + y**2 + 2*x*y
print(z)
print(temp)
print("-"*50)

# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
p = 5
q = 3
r = p**2 + q**2 - 2*p*q
print("(p+q)^2= ", r)
print("*"*50)

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
k = 5
l= 4
m = (k - l) * (k+l)
print("k^2-l^2 is equal to :" , m)
print("_"*50)

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
a = 3
b = 2
result = a**3-3*a*b*(a+b)+b**3
print("(a-b)^3: ",result)
print("_"*50)

# 13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a = 3
b = 2
result = a**3+3*a*b*(a+b)+b**3
print("(a+b)^3: ",result)
print("_"*50)
# 15). Python program to calculate the area of the square.
# Formula : area = a*a
side = 8
area = side  * side
print("The are of square is : ", area)

# 16). Python program to calculate the area of a circle.
# Formula = PI*r*r
# r = radius
PI = 22/7
radi = 21
ar = PI * radi**2
print("Area of circle is: ", ar)
print("_"*50)

# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a
s = 9
ar_cube = 6*s**2
print("area of a cube is : ",ar_cube)
print("_"*50)

# 18). Python program to calculate the area of the cylinder.
rad = 21
height = 14
PI= 21/7
ar_cylinder = 2*PI*rad*(rad+height)
print("The area of cylinder is : ", ar_cylinder)
print("_"*50)

# 20). Python program to calculate simple interest.
principle = 1200
rate = 5
time = 2
SI = principle * rate* time / 100
print("The simple interest is: ",SI)
amount = principle + SI
print(" The amount after two years is: ",amount)
print("_"*50)