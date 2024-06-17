num1 = 100
num2 = 200
print(num1 == num2)

if num1 == num2:
    print("Both values are equal :", num1, num2)
else:
    print("Both values are not equal :", num1, num2)


print("_"*50)
"""
# check give number is divisible by 3 or not
n1 = input("Please enter the number :")
print(n1, type(n1))

if int(n1)%3 == 0:
    print("The number is divisible by 3 :", n1)
else:
    print("The number can not divide by 3 :", n1)
"""


"""
# check given number is even or odd
temp = int(input("Please enter the number :"))
if temp%2 == 0:
    print("This is even number")
else:
    print("This is odd number")
"""
"""
# logical operator
cond1 and cond2 
True and True : True
False and True : False
True and False : False
False and False : False


cond1 or cond2
True or True : True
False or True : True
True or False : True
False or False : False

> : greater than operator
< : less than operator
>= : greater than equal to
<= : less than equal to
!= : not equal to
== : equal to

"""


# write a python program to check given number is divisible by 3 and 7
"""
num1 = int(input("Please enter the number :"))
if num1%3 == 0 and num1%7 == 0:
    print("The number can divide by 3 and 7")
else:
    print("The number can not divide by 3 and 7")
"""

"""
num1 = int(input("Please enter the number :"))
if num1%3 == 0 or num1%7 == 0:
    print("The number can divide by 3 or 7")
else:
    print("The number can not divide by 3 or 7")
"""

## write a python program to check given number is available in the list or not

temp = 22
list1 = [4, 6, 8, 2, 6, 50]
if temp in list1:
    print("Value is available in the list")
else:
    print("value is not available in the list")


# program1 : write a python program to check given is even the print square or value else cube of value
# program2 : write a python to check given number divisible 3 and 7 and not by 11


##############################

"""
if condition1:
    code
elif condition2:
    code
elif condition3:
    code
else:
    code
"""

print("_"*50)
a = 40
b = 500
c = 70

if a > b and a > c:
    print("a has greater value")
elif b > c and b > a:
    print("b has greater value")
elif c > a and c > b:
    print("c  has greater value")
else:
    print("No one has greater")

# Home Work
# Write a python program to print student result as per the marks

"""
Nested if condition

if cond1:
    code
    if cond2:
        code
    else:
        code
else:
    code

"""

print("_"*50)
# write a python program for interview process.
round1 = "pass"
round2 = "pass"
round3 = "fail"


if round1 == "pass":
    print("Congrats your first round is cleared")
    if round2 == "pass":
        print("Congrats your 2nd round is cleared")
        if round3 == "pass":
            print("Congrats you are selected")
        else:
            p+rint("Failed in 3rd round, try next time")
    else:
        print("Failed in 2nd round, try next time")
else:
    print("Failed in first round, try next time")


print("_"*50)
# write a if condition in one single line
n = 51
result = "even" if n%2 == 0 else "odd"
print(result)
