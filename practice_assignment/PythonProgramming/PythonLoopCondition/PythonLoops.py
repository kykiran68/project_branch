#range(initial value, end value, difference of values)
# The end value will always be excluded
# range(1, 10, 1) # 1 2 3 4 5 6 7 8 9
# range(1, 10, 2)  # 1 3 5 7 9

# default difference value is 1
# range(1, 10)  # 1 2 3 4 5 6 7 8 9

# default initial value is 0
# range(5)  # 0, 1, 2, 3, 4

for i in range(1, 10, 1):
    print(i)

print("_"*50)

# default difference value is 1
for i in range(1, 10):
    print(i)

print("_"*50)
for j in range(1, 10, 2):
    print(j)

# default initial value is zero and last value is 1
print("_"*50)
for i in range(5):
    print(i)

print("_"*40)
# print reverse order numbers
for i in range(10, 1, -1):
    print(i)


# print table of any given number
print("_"*50)
num = 6
for i in range(1, 11):
    print(num, "*", i ,":", i*num)


# write a if condition with loop
# get all the number which can divide by three
print("_"*50)
for i in range(1, 20):
    if i%3 == 0:
        print(i)

#### apply loop on string ###
print("_"*50)
str1 = "Good Morning"
for char in str1:
    print(char, end=" ")

# G o o d   M o r n i n g
print()
### apply loop on list  ###
print("_"*50)
list1 = [4, 7, 2, 8, 'Hello', 'Python', 'Learning']
for val in list1:
    print(val, end=" ")

print()

# write a python program to get factorial oo any number
# fact of 5 = 5*4*3*2*1
print("_"*50)
num = 6
fact = 1
for i in range(num, 0, -1):
    fact = fact*i # 5, 20, 60, 120, 120

print("Factorial output :", fact)


# write a python program to check given number is prime or not
print("_"*50)

#num = int(input("Please enter the number to check prime :"))
num = 15
prime = True

for i in range(2, num//2):
    print(i)
    if num%i == 0:
        prime = False
        break
    else:
        pass

if prime:
    print("This is prime number :", num)
else:
    print("This is not prime number :", num)


################# Nested loop Concept ########

for i in range(1 , 5):
    print("address :", i)
    for j in range(1, 4):
        print("package :", j)

    print("_"*40)


"""
*
* * 
* * *
* * * * 
* * * * *
"""

for i in range(1, 7):
    for j in range(i):
        print("*" ,end=" ")
    print()



"""
* * * * *
* * * *
* * *
* *
*
"""
"""
step1 : write a loop to print initial line to print * start with
        for i in range(6, 1):
            print("*", end=" ") 
step2 : to repeat above, add above code in nested loop
step3 : now modify the code to repeat in decreasing order
         for i in range(k , 1, -1)
            print("*", end=" ")

"""
print("_"*40)
temp = 1
for k in range(6, 1, -1):
    for i in range(k, 1, -1):
            print(temp, end="  ")
            temp += 1
    print()



print("_"*40)
temp = 65
for k in range(6, 1, -1):
    for i in range(k, 1, -1):
            print(chr(temp), end="  ")
            temp += 1
    print()


print(ord("a")) # 97

# small case ascii value : 97 - 122
# capital letter ascii value : 65-90

for i in range(97, 123):
    print(chr(i), end=" ")
print()
for i in range(65, 91):
    print(chr(i), end=" ")

print()
print("_"*50)
# write a program to remove the duplicate value from list
list1 = ['rahul', 'mahesh', 'rahul', 'ashok', 'mahesh']
count = 0
dict1 = {}

for val in list1:
    if val in dict1:
        #count += 1
        dict1[val] += 1
    else:
        #count = 0
        dict1[val] = 1

list1 = []
for k, v  in dict1.items():
    if v > 1 not in list1:
        list1.append(k)
    else:
        list1.append(k)

print("val1 :", list1)

###########################

list2 = ['rahul', 'mahesh', 'rahul', 'ashok', 'mahesh']
result = []
for val in list2:
    if val not in result:
        result.append(val)
    else:
        continue

print("result :", result)

############### solve with list comprehension #################
list3 = ['rahul', 'mahesh', 'rahul', 'ashok', 'mahesh']
output = []
[output.append(val) for val in list3 if val not in output]
print("result :" ,output)


############ BREAK , Continue, PASS ##########
print("_"*40)
for i in range(1, 11):
    if i == 3 or i == 4:
        continue
    print(i)


# break
print("_"*50)
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("_"*60)
# pass

for i in range(1, 6):
    if i == 4:
        pass
    print(i)
