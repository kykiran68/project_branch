# 1). Python program to check given number is divided by 3 or not.
a = int(input("Enter the number: "))
if a % 3 == 0:
    print("The number is divisible by 3 : ", a)
else:
    ("the number is not divisible by 3 ")
print("*"*40)

# 2). If else program to get all the numbers divided by 3 from 1 to 30.
b = int(input("Enter the number: "))
if 1 < b <= 30 and b%3 == 0:
    print("The number is divisible by 3 : ", b)
else:
    print("no. is not divisible or greater than 30")
print("*"*40)

'''# 3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks'''
marks = int(input("Enter the marks: "))
if 0 < marks < 40:
    print("you are fail in examination with marks", marks)
elif 40<= marks <= 60:
    print("you are passed with third division. your marks is ", marks)
elif 60 < marks <= 80:
    print("you are passed with second division. your marks is ", marks)
elif 80 < marks <= 100:
    print("congratulations! you are passed with first division. your marks is ", marks)
else:
    print("invalid marks")

# 4). Python program to check the given number divided by 3 and 5.
c = int (input("Enter the input : "))
if c%3 == 0 and c%5 == 0:
    print("The number is divisible by 3 and 5 : ", c)
else:
    print("The number is not divisible")

# 5). Python program to print the square of the number if it is divided by 11.
d = int (input("Enter the input : "))
if d%11 == 0:
    print("The number is divisible by 11. Square of number is : ",d**2)
else:
    print("The number is not divisible")

# 6). Python program to check given number is a prime number or not.
e = int (input("Enter the input : "))
prime = True
for i in range (2,e,1):
    if e%i ==0:
        prime = False
if prime == True:
    print("It is prime number")
else:
    print("It is not prime")

# 7). Python program to check given number is odd or even.
f = int (input("Enter the input : "))
if f%2 == 0:
    print("It is even number")
else:
    print("It is odd number")


# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Take input through the user
num = int(input("Enter a number: "))
# Check for number in fibonacci series
if num in fib:
# Print output
    print("It is a part of the series")
else:
# Print output
    print("It is not a part of the series")


# 9). Python program to check authentication with the given username and password.
user = "kiran"
pass_1 = "password"
if user == "kiran" and pass_1 == "password":
    print("Authentication successful")
else:
    print("Authentication unsuccessful")

# 10). Python program to validate user_id in the list of user_ids.
list1 = ["kiran", "rubi" , "ramesh", "shivam"]
input1 = input("Enter user id : ")
if input1 in list1:
    print("valid user id :", input1)
else:
    print("invalid user id")


# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
number = int(input("Enter the number : "))
if number%2 == 0:
    print("the square of the number is : ", number**2)
elif number%3 ==0:
    print("The cube of the number is : ", number**3)
else:
    print("The number is not divisible by 2 and 3")

# 12). Python program to describe the interview process.
round1 = "pass"
round2 = "fail"
round3 = "fail"
if round1 == "pass":
    print("you have cleard the round 1")
    if round2 == "pass":
        print("you have cleared the round 2")
        if round3 == "pass":
            print("welcome to company")
        else:
            print("you are not selected")
    else:
        print("you are not selected")
else:
    print("you are not selected")

# 13). Python program to determine whether a given number is available in the list of numbers or not.
list2 = [5,9,11,76,45,98]
no = int(input("enter number: "))
if no in list2:
    print("Number is available in list : ", no)
else:
    print("Number is not available in list")


# 16). Python program to check whether any given number is a palindrome.
p = (input("enter number: "))
if p == p[::-1]:
    print("It is palindrome")
else:
    print("It is not a palindrome")


# 19). Python program to check whether the given number is positive or not.
n = int(input("enter number: "))
if 0 < n:
    print("It is positive number")
else:
    print("It is negative number")

# 21). Python program to check whether the given number is positive or negative and even or odd.
nu = int(input("enter number: "))
if nu > 0:
    print("The number is positive")
    if nu%2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative")


# 23). Python program to check whether a given character is uppercase or not.
char = (input("enter character: "))
if "A" < char < "Z":
    print("This character is uppercase")
else:
    print("It is not uppercase character")

# 25). Python program to check whether the given number is an integer or not.
num1 = 54
if type(num1) == int:
    print("True")
else:
    print("False")


# 26). Python program to check whether the given number is float or not.
t = 6.8
if type(t) == float:
    print("It is float")
else:
    print("It is not float")


# 28). Python program to print all the numbers from 10-15 except 13
i = 10
for i in range(10,16,1):
    if i != 13:
        print("THE NUMBER: ", i)

'''29). Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill'''
unit = int(input("enter unit: "))
if 0 < unit < 50:
    print("your electricity bill is 0.50 pr unit")
elif 50<=unit<100:
    print("your electricity bill is 0.75 pr unit")
elif 100<=unit<250:
    print("your electricity bill is 1.25 pr unit")
elif 250<=unit:
    print("your electricity bill is 1.50 pr unit")
else:
    print("invalid no.")

# 30). Python program to check whether a given year is a leap or not.
year = int(input("enter year: "))
if year%100 == 0 and year>0:
    if year%400 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    if year%4 == 0 and year>0:
        print("It is a leap year")
    else:
        print("It is not a leap year")

# 32). Python program to check whether an alphabet is a vowel.
vow = input("enter alphabet: ")
if "AEIOUaeiou" in vow:
    print("It is vowel")
else:
    print("It is consonant")

# 34).  Python program to convert the month name to the number of days.
month = input("Enter month: ")
if month == "january":
    print("Number of days: 31")
elif month == "february":
    print("Number of days: 28/29")
elif month == "march":
    print("Number of days: 31")
elif month == "april":
    print("Number of days: 30")
elif month == "may":
    print("Number of days: 31")
elif month == "june":
    print("Number of days: 30")
elif month == "july":
    print("Number of days: 31")
elif month == "august":
    print("Number of days: 31")
elif month == "september":
    print("Number of days: 30")
elif month == "october":
    print("Number of days: 31")
elif month == "november":
    print("Number of days: 30")
elif month == "december":
    print("Number of days: 31")
else:
    print("Invalid month")

''' 35). Python program to check whether a triangle is equilateral or not.
36). Python program to check whether a triangle is scalene or not. 
37). Python program to check whether a triangle is isosceles or not.'''
side1 = int(input("enter side : "))
side2 = int(input("enter side : "))
side3 = int(input("enter side : "))
if side1 == side2 == side3:
    print("It is equilateral triangle")
elif side1 == side2 != side3 or side1 == side3 != side2 or side2 == side3 != side1:
    print("It is isosceles triangle")
elif side1 != side2 != side3:
    print("It is scalene triangle")
else:
    print("It is not a triangle")

# 39). Python program to check whether the input number is a float or not
# if yes then round up the number to 2 decimal places.
f = 87.9876
if type(f) == float:
    print(round(f, 2))
else:
    print("It is not float")

# 43). Python program to check whether two numbers are equal or not.
num1 = int(input("enter number1 : "))
num2 = int(input("enter number2 : "))
if num1 == num2:
    print("The number is equal")
else:
    print("Number is not equal")

# 44). Python program to check whether the given input is a complex type or not.
a = num = 5+6j
if type(num) == complex:
    print("True")
else:
    print("False")

# Check whether the given input is Boolean type.
num = True
if type(num) == bool:
    print("True")
else:
    print("False")

a=input("Enter a value : ")
if a in ("0","1","True","true","TRUE","False","FALSE","false"):
    print("it is a boolean value")
else:
    print("not a boolean value")

# 49). Python program to create 10 groups of numbers between 1-100
# and find out given input belongs to which group using python nested if else statements.
group = int(input("Enter a value : "))
if 1 < group <= 10:
    print("The number belongs to group 1")
elif 11 < group <= 20:
    print("The number belongs to group 2")
elif 21 < group <= 30:
    print("The number belongs to group 3")
elif 31 < group <= 40:
    print("The number belongs to group 4")
elif 41 < group <= 50:
    print("The number belongs to group 5")
elif 51 < group <= 60:
    print("The number belongs to group 6")
elif 61 < group <= 70:
    print("The number belongs to group 7")
elif 71 < group <= 80:
    print("The number belongs to group 8")
elif 81 < group <= 90:
    print("The number belongs to group 9")
elif 91 < group <= 100:
    print("The number belongs to group 10")
else:
    print("Number not belong to any group")

 #51). Take values of the length and breadth of a rectangle from the user and
#check if it is square or not using the python if else statement.
length = int(input("Enter a length : "))
breadth = int(input("Enter a breadth : "))
if length == breadth:
    print("It is a square")
else:
    print("It is a rectangle")

#52). A shop will give a 10% discount if the bill is more than 1000, and 20% if the bill is more than 2000.
# Using the python program Calculate the discount based on the bill.
bill = int(input("Enter a bill : "))
if 2000>bill>= 1000:
    print("your bill is: ", bill,"discount is: ", bill*10/100)
elif bill >= 2000:
    print("your bill is: ", bill,"discount is : ", bill * 20 / 100)
else:
    print("your bill is less")

# 53). Python program to print the absolute value of a number defined by the user.
abso = int(input("Enter a number : "))
print("The absolute value of number is : ",abs(abso))

# 55). Python program to check whether the last digit of a number defined by the user is divisible by 4 or not.
digit = int(input("Enter a number : "))
if digit[-1]%4 == 0:
    print("The last digit is divisible by 4:", digit)
else:
    print("The number is not divisible")

# 59). Python program to accept the city name and display its monuments (take Pune and Mumbai as cities).
city = input("Enter city name: ").lower()
if city == "pune":
    print("Shaniwar vada\nLal mahal\nSinhgad fort")
elif city == "mumbai":
    print("Getway of India\nGandhi statue\nAjanta cave")
else:
    print("Invalid city")

# 61). Python program to find the lowest number between three numbers.
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))
if num1>num2 and num1>num3:
    print("Number 1 is greater no")
elif num2>num1 and num2>num3:
    print("number 2 is greater")
else:
    print("number 3 is greater")

# 63). Python program to accept two numbers and mathematical operations from users
# and perform mathematical operations according to it.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operation = input("Enter operation of your choice")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "/":
    print(num1/num2)
elif operation == "*":
    print(num1*num2)
else:
    print("Invalid operation")

# 64). Python program to accept marks from the user allot the stream based on the following criteria.
marks = int(input("Enter marks: "))
if 85 <= marks <101:
    print("Stream alloted: Science")
elif 70 <= marks < 85:
    print("Stream alloted: Commerce")
elif 35 <= marks < 70:
    print("Arts")
elif 0 < marks < 35:
    print("Stream alloted: Fail")
else:
    print("Invalid marks")