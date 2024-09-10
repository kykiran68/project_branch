########## Integer ########

# int -> float
n1 = 45
print(type(n1), n1)  # <class 'int'> 45
f1 = float(n1)
print(type(f1), f1)  # <class 'float'> 45.0

# int -> string
n2 = 457
s2 = str(n2)
print(type(s2), s2 * 2, s2[1])
# <class 'str'> 457457

# int -> list # conversion is not possible
"""
print("_"*50)
n3 = 689
l1 = list(n3)
print(l1)
"""

# int ->  tuple # conversion is not possible
# int -> dict # conversion is not possible
# int -> set # conversion is not possible
# int -> boolean

num1 = 5
b1 = bool(num1)
print(b1)  # True

num2 = 0
b2 = bool(num2)
print(b2)  # False

num3 = -33
b3 = bool(num3)
print(b3)  # True

########################## Float ################
print("_" * 50)
# float -> int
var1 = 55.67
n1 = int(var1)
print(n1, type(n1))  # 55 <class 'int'>

#### float -> string ###
var2 = 45.66
s1 = str(var2)
print(s1, type(s1), ":", s1 * 2, ":", s1[-2])
# 45.66 <class 'str'> : 45.6645.66 : 6

# float -> list # conversion is not possible
# float -> dict # conversion is not possible
# float -> tuple # conversion is not possible
# float -> set # conversion is not possible
# float -> boolean

f1 = 44.34
b1 = bool(f1)
print(b1)  # True

f2 = 0.0
b2 = bool(f2)
print(b2)  # False

########### string ############

# string -> int

# if string contains character then conversion is not possible
"""
s1 = "Hello"
n1 = int(s1)
# invalid literal for int() with base 10: 'Hello'
print(n1)
"""

# if the string contains only number, then str to int conversion is possible
s2 = "5782"
n2 = int(s2)
print(n2, type(n2), n2 * 2)
# 5782 <class 'int'> 11564


#### string - float ####

# if string contains character then str to float conversion is not possible
# if string contains only number or pointer values then conversion is possible
s3 = "55.789"
f3 = float(s3)
print(f3, type(f3), ":", f3 * 2)
# 55.789 <class 'float'> : 111.578

### string ->  list ####
print("_" * 50)
str_a = "Python"
l1 = list(str_a)
print(l1, type(l1))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>

### string -> tuple #####
str_b = "Programming"
t1 = tuple(str_b)
print(t1, type(t1))
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple'>

### string -> dict ####
print("_" * 50)

"""
# If string contains any plain word, then str to dict conversion is not possible
str_c = "Hello"
d1 = dict(str_c)
print(d1, type(d1))
# dictionary update sequence element #0 has length 1; 2 is required
"""

import json

str_g = '{"Name" : "John", "Phone" : 765756657, "email" : "john@gmail.com"}'
dict_output = json.loads(str_g)

print(dict_output, type(dict_output))
# {'Name': 'John', 'Phone': 765756657, 'email': 'john@gmail.com'} <class 'dict'>

print(dict_output['email'])
# john@gmail.com

### string -> set ####
print("_" * 50)
str_j = "Python Programming"
set1 = set(str_j)
print(set1, type(set1))
# {'n', 'h', ' ', 'r', 'm', 'i', 'a', 'P', 't', 'y', 'g', 'o'} <class 'set'>

### string -> boolean ####

str_k = ""
b1 = bool(str_k)
print(b1)  # False

str_l = "Hello"
b2 = bool(str_l)
print(b2)  # True

############################# List ######################

### list  -> int #### conversion is not possible
### list -> float ### conversion is not possible
### list -> string ###

l1 = [5, 7, 8, 9]
s1 = str(l1)
print(s1, type(s1))  # [5, 7, 8, 9] <class 'str'>
print(s1[0], s1[1], s1[2], s1[-1])  # [ 5 , ]

#### list -> tuple ###
print("_" * 50)
l2 = [6, 8, 9, 2]
t2 = tuple(l2)
print(t2, type(t2), t2[0])
# (6, 8, 9, 2) <class 'tuple'> 6

### list -> dict ####
print("_" * 50)
"""
l3 = [5, 8, 2, 6]
d1= dict(l3)
print(d1,type(d1))
 # TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""

lista = [66, 77, 72, 88]
listb = [3, 6, 8, 22, 99]

result = dict(zip(lista, listb))
print("result :", result)
# result : {'a': 3, 'b': 6, 'c': 8, 'd': 22}
# result : {66: 3, 77: 6, 72: 8, 88: 22}


####### list -> set ##########
print("_" * 50)
list1 = [4, 6, 8, 4, 6, 2, 4]
s1 = set(list1)
print(s1, type(s1))
# {8, 2, 4, 6} <class 'set'>

print(list(s1))  # [8, 2, 4, 6]

##### list -> Boolean #######
list1 = [5, 7, 8]

b1 = bool(list1)
print(b1)  # True

list2 = []
b2 = bool(list2)
print(b2)  # False

################### Tuple ###################

print("_"*50)
# tuple -> int  # conversion is not possible
# tuple -> float # conversion is not possible
# tuple -> string
tup1 = (5, 6, 8, 2)
str1 = str(tup1)
print(str1, type(str1), str1[0], str1[1])
# (5, 6, 8, 2) <class 'str'> ( 5

# tuple -> list
tup2= (7, 8, 2, 4)
list1 = list(tup2)
print(list1, type(list1), list1[0])
# [7, 8, 2, 4] <class 'list'> 7

### tuple -> dict ### conversion is not possible
### tuple -> set ###
print("_"*40)
tup3 = (5, 8, 3, 8, 3, 7, 2)
set1 = set(tup3)
print(set1,type(set))
#{2, 3, 5, 7, 8} <class 'type'>

### tuple -> boolean ####

tup3 = (4, 7, 9)
print(tup3, type(tup3))
b1 = bool(tup3)
print(b1) # True

tup4 = ()
b2 = bool(tup4)
print(b2) # False

################ Dictionary ###########

# dict -> int : conversion is not possible
# dict -> float : conversion is not possible
### dict -> string ###

dict1 = {'a' : 123, 'b' : 456}
s1 = str(dict1)
print(s1, type(s1), s1[0], s1[-2])
# {'a': 123, 'b': 456} <class 'str'> { 6

### dict -> list ###
print("_"*50)
dict2 = {'Name' : 'john', 'email' : 'john@gmail.com', 'phone' : 3456656}
l1 = list(dict2)
print(l1)
# ['Name', 'email', 'phone']


##### dict -> tuple ###
print("_"*50)
dict2 = {'Name' : 'john', 'email' : 'john@gmail.com', 'phone' : 3456656}
t1 = tuple(dict2)
print(t1, type(t1))
# ('Name', 'email', 'phone') <class 'tuple'>

### dict -> set ####
dict2 = {'Name' : 'john', 'email' : 'john@gmail.com', 'phone' : 3456656}
s1 = set(dict2)
print(s1, type(s1))
# {'Name', 'phone', 'email'} <class 'set'>

#### dict -> boolean ###
print("_"*40)
dict1= {}
b1= bool(dict1)
print(b1) # False

dict2 = {'a' : 456}
b2 = bool(dict2) # True
print(b2)

######################## Set #############

# set -> int : conversion is not possible
# set -> float : conversion is not possible
### set -> string ####
print("-"*40)
set1 = {5, 8, 9, 2, 6}
str1 = str(set1)
print(str1, type(str1), str1[0], str1[1])
# {2, 5, 6, 8, 9} <class 'str'> { 2

### set1 -> list ####
seta = {5, 8, 9, 2, 6}
lista = list(seta)
print(lista, type(lista))
# [2, 5, 6, 8, 9] <class 'list'>

#### set -> tuple ####
setb = {6, 8, 2, 56, 3}
tup1 = tuple(setb)
print(tup1, type(tup1))
# (2, 3, 6, 8, 56) <class 'tuple'>

#### set -> dictionary ### conversion is not possible
#### set -> boolean ####

set1 = {5, 7, 8}
b1 = bool(set1)
print(b1) # True

set2 = set()
b2 = bool(set2)
print(b2)  # False


