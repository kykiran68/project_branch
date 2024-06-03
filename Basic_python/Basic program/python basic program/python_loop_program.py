# 1). Write a Python loops program to find those numbers which are divisible by
# 7 and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500,2701):
    if i %7 == 0 and i%5 == 0:
        print("It is divisible by 5 and 7 : ",i)

# 2). Python Loops program to construct the following pattern, using a nested for loops.
l1 = int(input("Enter the input"))
for l1 in range(1,l1):
    print("*"*l1)
for l1 in range(l1,0,-1):
    print("*"*l1)

# 3). Python Loops program that will add the word from the user to the empty string using python.
word = input("Enter the word: ")
str1 = ""
for i in range(len(word)):
    str1 += word[i]

print(str1)


# 4 Python Loops program to count the number of even and odd numbers from a series of numbers using python.
num_1 = int(input("Enter the first no"))
num_2 = int(input("Enter the first no"))
even = 0
odd = 0
for i in range(num_1,num_2):
    if i%2 == 0:
        even = even+1
    else:
        odd = odd+1
print(even,odd)


# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
i = 0
while i<6:
    if i!=3 and i!=6:
        print(i)
    i = i+1

# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
i=1
j=1
while i <=20:
    j = i+j
    j+1

# 7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
f1 = 1
while f1<=30:
    if f1%3==0:
        print("FIZZ",end=" ")
    elif f1%5==0:
        print("BUZZ",end=" ")
    else:
        print(f1,end=" ")
    f1=f1+1


# 8). Write a program that accepts a word from the user and
# converts all uppercases in the word to lowercase using python.
a = input("Enter a word: ")
b = " "
c=0
for c in range(len(a)):
    if a[c].isupper():
        b = b+a[c].lower()
    else:
        b = b+a[c].lower()
print(b)


# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.
a = input("Enter an input : ")
letter = 0
digit = 0
b = 0
while b < len(a):
    if a[b].isupper() or a[b].islower():
        letter = letter+1
    else:
        digit = digit+ 1
    b = b+1
print("letter : ",letter)
print("digit : ",digit)

# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
'''
  * * *  
*       *
*       *
*       *
*       *
*       *
  * * *  
   '''
for i in range(1, 6):
    if i == 1 or i == 5:
        print(" ", end=" ")
    else:
        print("*", end=" ")
print()

for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(1, 6):
    if i == 1 or i == 5:
        print(" ", end=" ")
    else:
        print("*", end=" ")


# 11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n = int(input("Enter the number: "))
for n in range(1,n+1):
    print(n,end=" ")


# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
num1 = int(input("Enter the number: "))
num2 = 1
while num1>= num2:
    print(num1, end=" ")
    num1 = num1 - 1


# 13). Python Loops program to print all alphabets from a to z using for loop
 #  Take chr method help to print characters with ASCII values

for alpha in range(65,90):
    print(chr(alpha), end=" ")
for alpha in range (97,127):
    print(chr(alpha), end=" ")
'''
* * * * *
* * * * *
* *
* *
* * * * *
* * * * *
'''
for i in range(1,3):
   print("* "*5)
for i in range(1,3):
   print("* "*2)
for i in range(1,3):
   print("* "*5)

# 14). Python Loops program to print all even numbers between 1 to 100 in python.
for i in range(1,101):
    if i%2 ==0:
        print("even no : ",i)

# 15). Python Loops program to print all odd numbers between 1 to 100 using python.
for i in range(1,101):
    if i%2 !=0:
        print("odd no : ",i)


# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
i = int(input("Enter the last number: "))
j = 0
for k in range(1,i+1):
    j = j+k
print(j)

# 17). Python program to find the sum of all even numbers between 1 to n using python.
i = int(input("Enter the last number: "))
j = 0
for k in range(1,i+1):
    if k%2 == 0:
        j = j+k
print(j)

# 18). Python Loops program to find the sum of all odd numbers between 1 to n using python.
i = int(input("Enter the last number: "))
j = 0
for k in range(1,i+1):
    if k%2 != 0:
        j = j+k
print(j)

# 19). Write a program to count the number of digits in a number using python.
i = input("Enter the number: ")
j = 0
for digit in i:
    j= j+1
print(j)


# 20). Write a program to find the first and last digits of a number using python.
i = input("Enter the number: ")
j = 0
for j in range(len(i)):
    k=(i[0],i[-1])
print(k)

# 21). Write a program to find the sum of the first and last digits of a number using python.
i = input("Enter the number: ")
j = 0
for j in range(len(i)):
    k=int(i[0])+int(i[-1])
print(k)


# 22). Write a program to calculate the sum of digits of a number using python.
num = int(input("Enter a number : "))
sum = 0
while num>0:
    rem = num%10
    sum = sum + rem
    num = num//10
print("Addition is :", sum)

# 23). Write a program to calculate the product of digits of a number using python
num = int(input("Enter a number : "))
mul = 1
while num>0:
    rem = num%10
    mul = mul* rem
    num = num//10
print("Multiplication is :", mul)
# 24).Python loops program to enter a number and print its reverse using python.
i = input("Enter the number: ")
j=int(i[::-1])
print(j)

# 25). Write a program to check whether a number is a palindrome or not using python loops.
num = int(input("Enter the input: "))
n=num
rnum=0
while num>0:
    digit = num%10
    rnum = (rnum*10)+digit
    num = num//10
if n == rnum:
    print("It is palendrome")
else:
    print("not palendrome")

# 26). Program to find the frequency of each digit in a given integer using Python Loops.
num1=int(input("enter a number :"))
str1=str(num1)
dict1={}
for i in str1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)

# 27). Python loops program to enter a number and print it in words.
num = int(input("Enter the number : "))
str1 = str(num)
for i in range(len(str1)):
    if str1[i] == "0":
        print("zero", end=" ")
    elif str1[i] == "1":
        print("one", end=" ")
    elif str1[i] == "2":
        print("two", end=" ")
    elif str1[i] == "3":
        print("three", end=" ")
    elif str1[i] == "4":
        print("four", end=" ")
    elif str1[i] == "5":
        print("five", end=" ")
    elif str1[i] == "6":
        print("six", end=" ")
    elif str1[i] == "7":
        print("seven", end=" ")
    elif str1[i] == "8":
        print("eight", end=" ")
    elif str1[i] == "9":
        print("nine", end=" ")
    else:
        print("invalid")


# 28). Python loops program to find the power of a number using Python for loop.
# Take values as an input base number and power, and get the total value using a loop.
num = int(input("enter number : "))
power = int(input("enter power : "))
result = 1
for i in range(power):
    result = result * num
print(result)


# 29). Python loops program to find all factors of a number using Python. Get all the numbers that can divide this number from 1 to n.
num = int(input("enter number : "))
for i in range(1,num+1):
    if num%i ==0:
        print(i,end=" ")


# 30). Write a program to calculate the factorial of a number using Python Loops.
num = int(input("E nter a number : "))
i =1
for j in range(num,0,-1):
    i = i*j
print(i)

num = int(input("E nter a number : "))
i =1
j =1
while j <=num:
    i = i*j
    j = j+1
print(i)


# 31). Write a program to check whether a number is a Prime number or not using Python Loops.
num = int(input("Enter a number : "))
for i in range(2, num):
    if num % i == 0:
        print("It is not prime")

    else:
        print("It is prime")


# 32). Write a program to print all Prime numbers between 1 to n using Python Loops.
num = int(input("E nter a number : "))
for i in range(2,num):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count +=1
    if count ==0:
        print(i,end=" ")


# 33). Python loops program to find the sum of all prime numbers between 1 to n using Python.
num = int(input("enter a number : "))
out =0
for i in range(2,num+1):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count+=1
    if count == 0:
        out+=i
print(out)

# 34). Python loops program to find all prime factors of a number using Python Loops.
num = int(input("Enter your number to get prime factor : "))
for i in range(1,num+1):
    if num%i ==0:
        count = 0
        for j in range(1,i+1):
            if i%j ==0:
                count+= 1
        if count == 2:
            print(i)


# 35). Python loops program to check whether a number is an Armstrong number or not using Python Loops.
num = int(input("enter a number : "))
num2 = str(num)
v = 0
for i in num2:
    v+=int(i)**len(num2)
if v == num:
    print("It is armstrong number")
else:
    print("Not a armstrong number ")


# 36). Python loops program to print all Armstrong numbers between 1 to n using Python Loops.


# 37). Write a program to check whether a number is a Perfect number or not using Python.
# Get factors of any number and the sum of those factors should be equal to the given number.
# The factor of 28: 1, 2, 4, 7, 14, and their sum is 28.

num = int(input("Enter a number: "))
output = 0
for i in range(1,num):
    count = 0
    if num%i == 0:
        count+=1
        output = output+i
if output == num:
    print("It is perfect number : ",num )
else:
    print("It is not perfct number : ",num)


# 38). Python loops program to print all Perfect numbers between 1 to n using Python.


# 39). Python loops program to print the Fibonacci series up to n terms using Python Loops.


# 40). Python loops program to print the multiplication table of any number using Python Loops.
num = int(input("Enter your input : "))
for i in range(1,11):
    output = i*num
    print(num,"*",i,"=",output)



# 41).  Python loops program to print the pattern T using Python Loops.
'''
* * * * * * * * *
* * * * * * * * *
      * * *
      * * *
      * * *
      * * *
      * * *
'''
for i in range(1, 3):
    for j in range (1,10):
        print("*" , end=" ")
    print()
for i in range(1,6):
    for j in range(1,10):
        if j ==4 or j==5 or j==6:
            print('*', end=" ")
        else:
            print(' ',end=' ')
    print()


# 42).  Write a program to print number patterns using Python Loops.
num = 1
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()
for i in range(5, 0, -1):
    for j in range(i-1):
        print(num,end=" ")
        num -= 1
    print()


# 43). Write a program to print the pattern A using Python Loops.


'''
      * * * 
    * * * * *
    * *   * *
    * *   * *
    * * * * *
    * * * * *
    * *   * *
    * *   * *
    * *   * *
'''
for i in range(5):
    if i == 0 or i == 4:
        print(" ", end=" ")
    else:
        print('*', end=" ")
print()
for i in range(5):
    print('*', end=" ")
print()
for j in range(2):
    for i in range(5):
        if i == 2:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
for j in range(2):
    for i in range(5):
        print("*", end=" ")
    print()
for j in range(3):
    for i in range(5):
        if i == 2:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()


# 44). Write a program to print the pyramid structure using Python Loops.
i = int(input("Enter your range : "))
for j in range(i):
    for k in range(i-j-1):
        print(" ",end=" ")
    for l in range(j*2+1):
        print("*",end=" ")
    print()


# 45). Write a program to count total numbers of even numbers between 1-100 using Python Loops.
count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += 1
        print(i, end=" ")

print("\n The total even number is : ", count)


# 46). Write a program to count the total numbers of odd numbers between 1-100 using Python Loops.
count = 0
for i in range(1, 101):
    if i % 2 != 0:
        count += 1
        print(i, end=" ")

print("\n The total odd number is : ", count)


# 47). Write a program to get input from the user if it is a number insert it into an empty list using Python Loops.
num = input("Enter a string : ")
list1 = []
for word in num:
    if word.isnumeric():
        list1.append(word)
print(list1)


# 48). Write a program to get input from the user if it is a string insert it into an empty list using Python Loops.
num = input("Enter a string : ")
list1 = []
for word in num:
    if word.isalpha():
        list1.append(word)
print(list1)

'''
# 49). Write a program to accept the kilometers covered and calculate the bill
# according to the following using Python Loops.
First 5 km- 15rs/km
Next 20 km- 12rs/km
After that- 10rs/km
'''
km = int(input("Enter the KM covered: "))
bill = 0
a=b=c=0
for i in range(1,km+1):
    if i<6:
        a += 1
    elif i>5 and i<26:
        b += 1
    elif i>25:
        c += 1

bill = a*5 + b*12 + c*10
print("Total bill: ", bill)


# 50). Write a program to input electricity unit charges
# calculate the total electricity bill according to the given condition using Python Loops.
'''For the first 50 units Rs. 0.50/unit.
For the next 100 units Rs. 0.75/unit.
For the next 100 units Rs. 1.25/unit.
For units above 250 Rs. 1.50/unit.
An additional surcharge of 17% is added to the bill.  '''
first = 0
second = 0
third = 0
forth = 0
bill = 0
dist = int(input("Enter the electrict unit : "))
for i in range(1,dist+1):
    if i <= 50:
        first = i*0.50
    elif 50< i<=100:
        second = i*0.75
    elif 100<i<=250:
        third = i*1.25
    elif 250<i:
        fourth = i*1.50
bill = first+second+third+forth
total = bill+((bill*17)/100)
print('the total bill is : ',total)


# 51). Write a program to calculate the sum of all odd numbers between 1-100 using Python Loops.
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        total = total+i
print(total)


# 52). Find the numbers which are divisible by 5 in 0-100 using Python Loops.
count = 0
for i in range(1, 101):
    if i % 5 == 0:
        count += 1
        print(i, end=" ")


#  53). Write a program to construct the following pattern, using a for loop in Python.
'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(1,6):
    print("* "*i)


# 54). Write a program to construct the following pattern, using a for loop in Python.
'''
* * * * *
* * * *
* * *
* *
*
'''
for i in range(6,0,-1):
    print("* "*i)


#  55). Write a program to construct the following pattern, using a nested for loop in Python.
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()


#  56). Write a program to get the Fibonacci series between 0 to 10 using Python Loops.




# 57). Write a program to check the validity of password input by users using Python Loops.
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 5 characters.
# Maximum length 15 characters.
password = input(
    "Enter your password (Minimum length 5 characters : ")

# Check if password length is between 5 and 15 characters
if 5 <= len(password) <= 15:
    # Check if password contains at least 1 lowercase letter, 1 uppercase letter, 1 digit, and 1 special character
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '@$&#' for char in password)

    if has_lowercase and has_uppercase and has_digit and has_special:
        print("Password is valid.")
    # break
    else:
        print("Password does not meet the requirements.")
else:
    print("Password length should be between 5 and 15 characters.")


# 58). Write a program to check whether a string contains an integer or not using Python Loops.
str1 = input("Enter your input : ")
count = 0
for digit in str1:
    if digit.isnumeric():
        count += 1
    else:
        count = 0
if count > 0:
    print(True)

else:
    print(False)


# 59). Write a program to print the following pattern using Python Loops.
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
for i in range(1,6):
    print(" * "*i)
for i in range(4,0,-1):
    print(" * "*i)


# 60). Write a program to print a table of 5 using for loop using Python Loops.
num = int(input("Enter your number to print table : "))
for i in range(1,11):
    print(num," * ",i, " = ",num*i)


# 61). Write a program to print the first 20 natural numbers using for loop in Python.
for i in range(1,21):
    print(i,end=" ")


# 62). Write a program to display numbers from a list using Python Loops.
input1 = [1,5,8,0,4]
for i in input1:
    print(i,end=",")


# 63). Write a program to print each word in a string on a new line using Python Loops.
input1 = 'Sqatools'
for i in input1:
    print(i,end='\n')


# 64). Write a program to create an empty list and add even numbers from 1-10 in it including 10 using Python Loops.
l=[]
for i in range(1,11):
    if i%2 == 0:
        l.append(i)
print(l)


# 65). Write a program to create an empty list and add odd numbers from 1-10 in it including 1 using Python.
l=[]
for i in range(1,11):
    if i%2 != 0:
        l.append(i)
print(l)


# 66). Write a program to print the keys of a dictionary using Python Loops.
input1 = {'name':'virat','sports':'cricket'}
for key,value in input1.items():
    print(key,end=",")


# 67). Write a program to print the values of the keys of a dictionary using Python.
input1 = {'name':'virat','sports':'cricket'}
for key,value in input1.items():
    print(value,end=",")


# 68). Write a program to print the keys and values of a dictionary using Python Loops
input1 = {'name':'virat','sports':'cricket'}
for key,value in input1.items():
    print(key,value)


# 71). Find the sum of the first 10 natural numbers using the while loop in Python Loops.
output =0
for i in range(1,11):
    output+=i
print(output)


# 72). Find the multiplication of the first 10 natural numbers using Python Loops.
output =1
for i in range(1,11):
    output*=i
print(output)


# 73). Print numbers from 1-10 except 5,6 using a while loop in Python.
for i in range(1,11):
   if i !=5 and i !=6:
        print(i)


# 74). Write a program to print the days in a week except Sunday using a while loop in Python.
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday"
       ,"Friday","Saturday"]

for day in days:
    if day != "Sunday":
        print(day, end=" ")


# 75). Write a program to find the total number of special characters in a string using Python Loops.
input1 = input("Enter the string  : ")
count = 0
s_count =0
str1 =''
for word in input1:
    if word.isalnum():
        count += 1
    else:
        s_count+=1
        str1+=word
print(s_count)
print(str1)


# 76). Write a program to add even numbers in an empty list from a given list using Python Loops.
input1 = [2,3,5,76,9,0,16,]
l =[]
for word in input1:
    if int(word)%2 == 0:
        l.append(word)
print(l)


# 77). Write a program to add odd numbers in an empty list from a given list using Python Loops.
input1 = ['j','2','3','5','76','9','0','16','k']
l =[]
for word in input1:
    if word.isnumeric() and int(word)%2 != 0:
        l.append(word)
print(l)


# 78). Write a program to add special characters in an empty list from a given list using Python Loops.
input1 = ['s','2','4','6','a','@','!','%','#']
l =[]
for word in input1:
    if word.isalnum():
        pass
    else:
        l.append(word)
print(l)


# 79). Write a program to print the last element of a list using a while loop using Python Loops.
input1 = input("Enter a string : ")
print(input1[-1])
input1 = ['a',2,'7','h']
print(input1[-1])


# 80). Write a program to print 1-10 natural numbers but it should stop when the number is 6 using a while loop in Python.
count = 1

while count < 11:
    print(count)
    count += 1
    if count == 6:
        break


# 82). Write a program to count the total number of characters in a file using Python Loops.
char = 0
f = open("read_loop_file","r")
data = f.read()
for i in data:
    if i.isalpha():
        char+=1
f.close()
print(char)



# 83). Write a program to find the total number of digits in a file using Python Loops.
char = 0
f = open("read_loop_file","r")
data = f.read()
for i in data:
    if i.isdigit():
        char+=1
f.close()
print(char)


# 84). Write a program to find the total number of Uppercase letters in a file using Python Loops.
char = 0
f = open("read_loop_file","r")
data = f.read()
for i in data:
    if i.isupper():
        char+=1
f.close()
print(char)


# 85). Write a program to find the total number of special characters in a file using Python Loops.
char = 0
str1=""
f = open("read_loop_file","r")
data = f.read()
for i in data:
    if i.isalnum():
        pass
    else:
        char+=1
        str1+=i
f.close()
print(char)
print(str1)


# 86). Write a program to sort a list using for loop in Python Loops.
input1 = [6,8,2,3,1,0,5]
input1.sort()
print(input1)


# 87). Write a program to add elements from one list to another list and print It in descending order using Python Loops.
input1 = [2,5,8,0,1,4]
input1.sort()
print(input1[::-1])


# 87). Write a program to add elements from one list to another list and
# print It in descending order using Python Loops.
input1 = [2,5,8,0,1,4]
input1.sort()
l =[]
for i in input1:
    l.append(i)
l.reverse()
print(l)


# 88). Write a program to find the maximum number from the list using Python Loops
input1 = [12,14,45,88,63,97,88]
print(max(input1))


# 89). Print the following camel letter pattern using Python Loops.
# Part1 : First will print triangle of numbers in increasing order.
num1 = 65
for i in range(5):
    for j in range(i+1):
        print(chr(num1), end=" ")
        num1 += 1
    print()

# Part2 : Second will print triangle of number is decreasing order.
for k in range(5, 0, -1):
    for l in range(k-1):
        num1 += 1
        print(chr(num1), end=" ")
    print()


# 90). Print the following small alphabet letter pattern using Python Loops.
char = 97
var1 = 4
var2 = 4

for i1 in range(7):
    if i1 < 4:
        var1 = var1 - 1
        var2 = var2 + 1

        for j1 in range(9):

            if j1 > var1 and j1 < var2:

                print(chr(char), end=" ")
                char += 1
            else:
                print(" ", end=" ")
        print()

        # var1 = var1 - 1
        # var2 = var2 + 1
    else:
        var1 = var1 + 1
        var2 = var2 - 1
        for k in range(9):

            if k > var1 and k < var2:

                print(chr(char), end=" ")
                char += 1
            else:
                print(" ", end=" ")
        print()