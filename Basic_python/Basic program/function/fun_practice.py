# 1). Python function program to add two numbers.

def addition(num1,num2):
    print(num1+num2)
addition(50,40)
########################################################
def addition(num1,num2):
    print(num1+num2)
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
addition(x,y)


# 2). Python function program to print the input string 10 times.
def str1(n):
    print(n*10)
n = input('enter a string : ')
str1(n)


# 3). Python function program to print a table of a given number.
def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
num = int(input("Enter a number : "))
table(num)


# 4). Python function program to find the maximum of three numbers.
def maximum(a,b,c):
    if a>b and a>c:
        print("A is greater : ",a)
    elif b>a and b>c:
        print("B is greater : ",b)
    elif c>a and c>b:
        print("C is greater : ",c)
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))
maximum(num1,num2,num3)


# 5). Python function program to find the sum of all the numbers in a list.
def sum(num1):
    output =0
    for i in num1:
        output+=int(i)
    print(output)
num1 = list(input("Enter a number : ").split(","))
sum(num1)


# 6). Python function program to multiply all the numbers in a list.
def multiplication(n):
    output = 1
    for i in n:
        output = output*int(i)
    print(output)
n = list(input("Enter a list : ").split(','))
multiplication(n)


# 7). Python function program to reverse a string.
def reverse1(n):
    output=n[::-1]
    print(output)
n = input("Enter a string : ")
reverse1(n)

# 8). Python function program to check whether a number is in a given range.
def number(n):
    if 0 < n < 100:
        print("It is in given range : ",n)
    else:
        print("Number is out of range!!! ")
num = int(input("Enter the number : "))
number(num)


# 9). Python function program that takes a list and returns a new list with unique elements of the first list.
def unique_num(n):
    print(set(n))
num = list(input("Enter the number : ").split(","))
unique_num(num)


# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.
def prime_num(n):
    count = 0
    for i in range(2,n):
        if n%i ==0:
            count+=1
    if count ==0:
        print("It is a prime number : ",n)
    else:
        print("It is not prime")
num = int(input("Enter the number : "))
prime_num(num)


# 11). Python function program to find the even numbers from a given list.
def even_num(n):
    if n%2 == 0:
        print("It is even number : ",n)
    else:
        print("It is odd number ")
num = int(input("Enter the number : "))
even_num(num)


# 12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
def square_num(*args):
    for args in range(1,11):
        print(args**2,end=" ")

square_num(1,2,3,4,5,6,7,8,9,10)


# 13). Python function program to execute a string containing Python code.
v = '''
x = 2
y =5
print(x+y)
'''
exec(v)
print(v)


# 14). Python function program to access a function inside a function.
def add(a,b):
    def sub(c):
        nonlocal a,b
        return a+b-c
    return sub
resu = add(10,5)
print(resu(9))


# 15). Python function program to find the LCM of two numbers.
def lcm(n1,n2):
    if n1>n2:
        greater = n1
    else:
        greater = n2
    while(True):
        if greater%n1 ==0 and greater%n2==0:
            lcm = greater
            break
        greater+=1
    print("The lcm of numbers is : ",lcm)
num1 = int(input("Enter your first number : "))
num2= int(input("Enter your second number : "))
lcm(num1,num2)



# 16). Python function program to calculate the sum of numbers from 0 to 10.
def sum1():
    s =0
    for i in range(1,11):
        s +=i
    print("The sum of numbers is : ",s)
sum1()



# 17). Python function program to find the HCF of two numbers.
def hcf(n1,n2):
    if n1<n2:
        smaller = n1
    else:
        smaller = n2
    while(True):
        if n1%smaller ==0 and n2%smaller==0:
            hcf = smaller
            break
        smaller -= 1
    print("The lcm of numbers is : ",hcf)
num1 = int(input("Enter your first number : "))
num2= int(input("Enter your second number : "))
hcf(num1,num2)



# 18). Python function program to create a function with *args as parameters.
def cube(*args):
    for num in args:
     print(num**3,end=" ")
cube(2,6,9,4)



# 19). Python function program to get the factorial of a given number.
def fact(n):
    j =1
    for i in range(n,1,-1):
        j = j*i
    print("The factorial of number is : ",j)
n = int(input("Enter your number to get factorial : "))
fact(n)


# 20). Python function program to get the Fibonacci series up to the given number.
def feb():
    i=0
    j=1
    c=0
    #while c<10:
    for c in range(0,11):
        print(i,end="  ")
        n1=i+j
        i=j
        j=n1
        #c+=1
feb()


#  21). Python function program to check whether a combination of two numbers has a sum of 10
def comb(num, output):
    for i in num:
        for j in range(i + 1):  # and j<=len(i):
            if i + j == output:
                print(True)
                return
    print(False)


comb([2, 5, 6, 4, 7, 3, 8, 9, 1], 10)



# 22). Python function program to get unique values from the given list.
def unique(num):
    a=set(num)
    print(list(a))
unique([4, 6, 1, 7, 6, 1, 5])



# 23). Python function program to get the duplicate characters from the string.
def unique(word):
    list1 = []
    for char in range(len(word)):
        for i in range(char+1,len(word)):
            if word[char] == word[i] and word[char] not in list1:
                list1.append(word[char])
    print(list1)
word = input("Enter your string : ")
unique(word)


# 24). Python function program to get the square of all values in the given dictionary.
def square(input1):
    d ={}
    for key,val in input1.items():
        d[key] = (val**2)
    print(d)
input1 = {'a': 4, 'b' :3, 'c' : 12, 'd': 6}
square(input1)


# 25). Python function program to create dictionary output from the given string.
def dictionary(input1):
    d ={}
    for key in input1:
        ele =key[0] + key[-1]
        d[ele] = (key)
    print(d)
input1 = "Python is easy to Learn".split()
dictionary(input1)


# 26). Python function program to print a list of prime numbers from 1 to 100.
def prime():
    list1 = []
    for i in range(1,101):
        count =0
        for j in range(1,i):
            if i%j == 0:
                count+=1
        if count ==1:
            print(i,end=" ")
prime()



# 27). Python function program to get a list of odd numbers from 1 to 100.
def odd(lower, upper):
    for i in range(lower, upper + 1):
        if i % 2 != 0:
            print(i, end=" ")


lower = int(input("Enter your lower range : "))
upper = int(input("Enter your upper range : "))
odd(lower, upper)


# 28). Python function program to print and accept login credentials.
def credential(user,password):
    username="kirankumari"
    password1 = "Kiran@123"
    if username == user:
        if password == password1:
            print("Login successfull!!")
        else:
            print("Invalid password")
    else:
        print("Invalid username")
user=input("Enter your username : ")
password = input("Enter your password : ")
credential(user,password)


# 29). Python function program to get the addition with the return statement.
def addition(a,b):
    return a+b
a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
print(addition(a,b))



# 30). Python function program to create a Fruitshop Management system.
def fruitshop(fruitname,quantity,price):
    print("The fruit name is : ",fruitname)
    print("Enter the quantity : ",quantity)
    print("Enter the price of fruit : ", price)
    print("The total bill is : ",quantity*price)
fruitshop('mango',5,10)


# 31). Python function program to check whether the given year is a leap year.
def leapyear(year):
    if year%100==0:
        if year%400==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        if year % 100!=0:
            if year%4 ==0:
                print("IT is a leap year")
            else:
                print("It is not a leap year")
leapyear(2007)



# 32). Python function program to reverse an integer.
def reverse(n):
    k=0
    while n>0:
        rem = n%10
        k=k*10+rem
        n=n//10
    print(k)
reverse(199)




# 33). Python function program to create a library management system.
def library(bname,cname):
    print("Book name: ",bname)
    print("Borrowed by :",cname)
library("Harry potter","Atharv")



# 34). Python function program to add two Binary numbers.
def binary(a,b):
    m = bin(int(a,2)+(int(b,2)))
    print(m[2:])
binary('10111','1000101')


# 35). Python function program to search words in a string.
def string(s1,s2):
    if s2 in s1:
        print("Word exists in string")
    else:
        print("Word not exists in string")
m = input("Enter your string : ").split()
n = input("Enter word to search : ")
string(m,n)


# 36). Python function program to get the length of the last word in a string.
def string(s1):
    print(len(s1[-1]))
m = input("Enter your string : ").split()
string(m)



# 37). Python function program to get a valid mobile number.
def mobile(num):
    if len(str(num))==10:
        print("It is valid mobile number")
    else:
        print("It is not a valid mobile number")
num=int(input("enter your mobile number : "))
mobile(num)


# 38 Program to convert an integer to its word format
def to_number():
    num = int(input("Enter a number: "))
    str1 = ""

    for i in str(num):
        if i == "1":
            str1 += "One"
        elif i == "2":
            str1 += "Two"
        elif i == "3":
            str1 += "Three"
        elif i == "4":
            str1 += "Four"
        elif i == "5":
            str1 += "Five"
        elif i == "6":
            str1 += "Six"
        elif i == "7":
            str1 += "Seven"
        elif i == "8":
            str1 += "Eight"
        elif i == "9":
            str1 += "Nine"

    print(str1)
to_number()



#