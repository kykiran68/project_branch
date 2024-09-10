"""
Properties:
-> dict store the data in form of key value pair
-  dict is mutable data type, we can modify at any point of time
-  dict only store unique keys, duplicate keys are not allowed.
-  Only immutable data type can be key in the dict, int, float, string, tuple, boolean
-  All type of data can be value in the dict.
"""

dict1 = {'a' : 3456, 'b' : 167}
print(dict1, type(dict1))
# {'a': 3456, 'b': 167} <class 'dict'>

dict1['c'] = 500
print(dict1)  # {'a': 3456, 'b': 167, 'c': 500}

# duplicate keys are not allowed, if user set the duplicate keys then will overwrite the previous value.
dict2 = {'a' : 111, 'b': 222, 'c' : 333, 'a' : 666}
print("dict2 :", dict2) # {'a': 666, 'b': 222, 'c': 333}


####### add all possible keys ##########

dict3 = {}
dict3[5] = 500
dict3[4.5] = "Hello"
dict3['Python'] = "Programming"
dict3[(3, 5, 7)]  = [4, 6, 8, 22, 33]
dict3[True] = (82, 33, 44)

print(dict3)
# {5: 500, 4.5: 'Hello', 'Python': 'Programming', (3, 5, 7): [4, 6, 8, 22, 33], True: (82, 33, 44)}

#dict3[[5, 6, 8]] = 654654
#print(dict3)
# TypeError: unhashable type: 'list'

# Get any value with the help of keys.
print(dict3['Python'])  #Programming



print("_"*50)
dict4 = {5: 500, 4.5: 'Hello', 'Python': 'Programming', (3, 5, 7): [4, 6, 8, 22, 33], True: (82, 33, 44)}

for val in dict4.items():
    print(val)

print("_"*50)

for k1, v1 in dict4.items():
    print("key :", k1)
    print("value :", v1)
    print("_"*5)

############################ Dictionary Methods #################

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

#########
# get() method : This method return the values on the basis of key provided.
dict1 = {'a' : 123, 'b' : 345, 'c' : 789}
val = dict1.get('b')
print("val of b :", val)
print("val of b :", dict1['b'])

########
print("_"*50)
# update() method : This method update the data from dict1 to dict2.
dict2 = {'Name' : 'Rahul', 'Age' : 30, 'Address' : 'Mumbai'}
dict2['Country'] = 'India'
print("dict2:", dict2)

dict3 = {'email' : 'rahul@gmail.com', 'phone' : 765765756}

dict2.update(dict3)
print("dict2 :", dict2)

############
# Keys() and value() method:
# keys() and values() method provide the list of keys and list of values from given dict.

dict_a = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com', 'phone': 765765756}

print(dict_a.keys()) # dict_keys(['Name', 'Age', 'Address', 'Country', 'email', 'phone'])
print(dict_a.values())  # dict_values(['Rahul', 30, 'Mumbai', 'India', 'rahul@gmail.com', 765765756])

###############
# items() method : This method provides list of key value combination in tuple
dict_b = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com', 'phone': 765765756}
print(dict_b.items())
# dict_items([('Name', 'Rahul'), ('Age', 30), ('Address', 'Mumbai'), ('Country', 'India'), ('email', 'rahul@gmail.com'), ('phone', 765765756)])


##############
print("_"*50)
# pop method : This method will remove data from dict with the help of keys.
dict_b = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com', 'phone': 765765756}

val = dict_b.pop('email')
print(val)
print("dictb:", dict_b)

#val2 = dict_b.pop() # pop expected at least 1 argument, got 0
#print(val2)

################
print("_"*50)
# popitems method : This method remove key value combination from the dictionary
dict_c = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com', 'phone': 765765756}

data = dict_c.popitem()
print(data) # ('phone', 765765756)
print("dict c:", dict_c)
# {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com'}

###############
dict1: {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala'}
#################
print("_"*50)
# clear method:

dict_d = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com', 'phone': 765765756}
dict_d.clear()
print("dict_d:", dict_d) # {}



dict_e = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai'}
#del dict_e
#print("dict_e :", dict_e) # name 'dict_e' is not defined


del dict_e['Address']
print("dict_e :", dict_e) #  {'Name': 'Rahul', 'Age': 30}
#######################
print("_"*50)
# copy method : this method copy data from dict1 to dict2

# shallow copy

dict1 =  {'a' : 345, 'b' : 678, 'c' : 999}
dict2 = dict1
dict2['d'] = 1000
print("dict1 :", dict1)
print("dict2 :", dict2)

# Deep copy
print("_"*40)
dictp =  {'a' : 345, 'b' : 678, 'c' : 999}
dictq = dictp.copy()
dictq['d'] = 300

print("dictp :", dictp) # dictp : {'a': 345, 'b': 678, 'c': 999}
print("dictq :", dictq) # dictq : {'a': 345, 'b': 678, 'c': 999, 'd': 300}




############################################
# program
list1 = ['a', 'b', 'c']
list2 = [22, 23, 44]
#dict1 = {'a' : 22, 'b' : 23, 'c' : 44}

output = {}
for i in range(len(list1)):
    output[list1[i]] = list2[i]

print("output :", output)


# program2:
str1 = "Python"
output= {'P': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n' : 6}

# program3:
str2 = "ProGraM"
list1 = [1, 2, 3, 4, 5, 6, 7]
output = {'p': 1, 'rr': 2, 'ooo': 3, 'gggg': 4, 'aaaaaa' : 6, 'mmmmmmm': 7}









