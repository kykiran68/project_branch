# Python Data Types
"""
1. Numbers
    i). Integer
    ii). Float
    iii). Complex Number

2. Sequential data type
    i). String
    ii). List
    iii). Tuple

3. Dictionary
4. Set
5. Boolean
"""

############# Integer Data Type ######

var1 = 50
var2 = 5456456456546546
var3 = 0

print(type(var1))
print(type(var2))
print(type(var3))

var4 = int()
print(type(var4), var4) # <class 'int'> 0

"""
Properties
 - Integer is immutable data type, once it is defined we can not change it.
 - There is no as such limit for integer data type. any long number we can defined as integer.
"""
a = 100
a = 200
a = 100+1


############# Float Data Type #############
print("_"*50)

vara = 56.55
varb = 0.0
varc = 43534534.34543534534534543
print(vara, type(vara)) # 56.55 <class 'float'>
print(varb, type(varb)) # 0.0 <class 'float'>
print(varc, type(varc)) # 43534534.34543534 <class 'float'>

"""
Properties
 - Float is immutable data type, once it is defined we can not change it.
 - There is no as such limit for float data type. any long number we can defined as float.
"""

############# Complex data type #############
print("_"*50)
"x+yj"
# x is real number
# y is imaginary number

var_1 = 10+50j
print(var_1, type(var_1))  # <class 'complex'>

var_2 = 40 + 60j
var3 = var_1 + var_2
print("var3 :", var3) # var3 : (50+110j)

var4 = 55.55 + 56.78j
print(var4, type(var4))  #(55.55+56.78j) <class 'complex'>

"""
Properties
 - complex number is the combination of real and imaginary number that's represent with x+yj
 - complex is the immutable data type, once it is defined we can not change it.
 - There is no as such limit for complex data type. any long number we can defined as complex values.
"""

############## Sequential data type ###########

##### String Data Type ###########
print("_"*50)
str1 = "H"
str2 = 'Python'
str3 = """
All Python releases are Open Source. 
Historically, most, but not all, 
Python releases have also been 
GPL-compatible. 
The Licenses page details 
GPL-compatibility and Terms and Conditions. 
"""

str4 = '''
This site hosts the "traditional" 
implementation of Python (nicknamed CPython). 
A number of alternative implementations are
'''

print(str1, type(str1))
print("_"*50)
print(str2, type(str2))
print("_"*50)
print(str3, type(str3))
print("_"*50)
print(str4, type(str4))


str5 = "Hello"
#  0  1   2  3  4   +ve indexing
#  H  E   L  L  O
# -5 -4  -3 -2 -1   -ve indexing

print(str5[1])   # e
print(str5[-4])  # e

"""
Properties
- String is immutable data type, can not change it once it is defined
- String follow positive and negative indexing to represent the data.
- String can be defined with single quote, double quote, triple quote as well.
"""

stra = "Python Programming"
strb = "Good Morning"
strc = stra + strb
print("strc :", strc)

# re-assignment of value in same variable
stra = "Python is Programming"

print(dir(str))


############## list data type ##############
print("_"*50)
list1 = [2, 3.5, 'Hello', [4, 6], (6, 8, 9), {'a' :123, 'b' : 444}]

print(list1, type(list1))
# [2, 3.5, 'Hello', [4, 6], (6, 8, 9), {'a': 123, 'b': 444}] <class 'list'>

list2 = []
print("list2 :", list2, type(list2))
# list2 : [] <class 'list'>

#        0   1   2   3   4    +ve indexing
list3 = [55, 77, 88, 22, 33]
#       -5  -4   -3  -2  -1   -ve indexing

print(list3[2])  # 88
print(list3[-1]) # 33

#        0  1          2          3
list4 = [5, [5, 7, 8], (2, 7, 9), 'Python']
#       -4  -3          -2         -1

print(list4[1])  # [5, 7, 8]
print(list4[1][1]) # 7
"""
# Properties
- List is mutable data type
- List follows positive and negative indexing as like string
- List can contain any type of data, int, float, string, list, dict, tuple, set, boolean
"""

list5 = [5, 7, 9]
list5.append(20)
print("list5 :", list5) # [5, 7, 9, 20]


######################### Tuple #######################
print("_"*50)
#       0  1  2  3
tup1 = (4, 7, 9, 10)
#      -4 -3 -2 -1

print(tup1, type(tup1))

print(tup1[2]) # 9

print(tup1[-3]) # 7

tup2 = (2, 3.5, (4, 5, 6), [2, 8, 3], 'Python', {'a' : 345, 'b' : 478})

print(tup2[3][1])  # 8
print(tup2[-2][-4])  # t
print(tup2[2][-1]) # 6
print(tup2[4][4])  # o

"""
properties :
 - tuple is immutable data type, can not changes once it is defined
 - tuple follows positive and negative indexing as like string and list
 - tuple can contains any type of data, int, float, string, list, tuple, dict, set, boolean
"""

print(dir(tuple))

################################# Dictionary #######################################
print("_"*50)
dict1 = {'Name' : 'Rahul', 'age' : 25, 'email' : 'rahul@gmail.com'}

print(dict1, type(dict1))
# {'Name': 'Rahul', 'age': 25, 'email': 'rahul@gamil.com'} <class 'dict'>

print(dict1['age'])  # 25
print(dict1['email']) # 'rahul@gmail.com'
dict1['city'] = 'Mumbai'

print(dict1)
# {'Name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 'city': 'Mumbai'}

dict1['age'] = 30
print(dict1)
# {'Name': 'Rahul', 'age': 30, 'email': 'rahul@gmail.com', 'city': 'Mumbai'}

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

"""
Properties :
-> dict is mutable data type, we can modify any point of time.
-> All the keys in the dict should be unique, duplicate keys are not allowed.
-> Only immutable data type can be in dict, int, float, string, tuple, boolean.
-> All type of data can value in the dict e.g. int, float, string, tuple, boolean, list, set, dict.
"""

dict2 = {}
dict2[50] = 100
dict2[5.5] = 55.55
dict2['Hello'] = "Good Morning"
dict2['a'] = [4, 6, 8]
dict2[(4, 7,  7, 2)] = ('a', 'b', 'c')
dict2[True] = False
print(dict2)

# list as key is not allowed
#dict2[[66, 7, 8]] = [55, 66, 77]
#print(dict2)
# int, float, string, tuple, boolean.

# dict2[{'a' : 123}] = 7000
# print(dict2)
# TypeError: unhashable type: 'dict'

# dict2[{5, 7, 8}] = {5, 8, 23, 33}
# print(dict2)
# TypeError: unhashable type: 'set'

####################### set #######################
print("_"*50)

set1 = {3, 55.55, 'Hello', (5, 7, 8), True, False, 3, 'Hello'}
print(set1)
set1.add(100)
print(set1)
"""
- properties :
- set only store unique data, duplicate data is not allowed.
- set is mutable data type, we can modify at any point of time.
- All the immutable data type can be member of set, like int, float, string, tuple, boolean
- Mutable data types are not allowed as member in the set, list, dict and set it self.
- Set store the data in random order.
- Set does not follow any indexing.
"""

######################## Boolean #######################

print("_"*50)
# boolean data type has only two values True and False

var1 = 60
var2 = 70
var3 = 60
print(var1 == var2) # False
print(var1 == var3) # True
















