# integer to float conversion
i1 = 45
print(i1, type(i1))
f1 = float(i1)
print(f1, type(f1))
print("*"*50)
# integer to string conversion
i2 = 65
s1 = str(i2)
print(s1, type(s1))
print("*"*50)
''' integer to list conversion is not possible
integer to dictionary conversion is not possible
integer to tuple conversion is not possible
integer to set conversion is not possible'''
# float to integer conversion
f2 = 99.55
int_1 = int(f2)
print(int_1, type(int_1))
print("*"*50)
# float to string conversion
f3 = 56.87
s2 = str(f3)
print(s2, type(s2))
print("*"*50)
''' float to list conversion is not possible
float to dictionary conversion is not possible
float to tuple conversion is not possible
float to set conversion is not possible'''
# string to integer conversion
# If the string is character then conversion is not possible.
s3 = "56789"
int_2 = int(s3)
print(int_2, type(int_2))
print("*"*50)
# string to float conversion
# If the string is character then conversion is not possible.
s4 = "56.789"
f4 = float(s4)
print(f4, type(f4))
print("*"*50)
# string to list conversion
str_a = "python"
l1 = list(str_a)
print(l1, type(l1))
print("*"*50)
# string to tuple conversion
str_b = "programming"
t1 = tuple(str_b)
print(t1, type(t1))
print("*"*50)
# string to dictionary conversion
import json
str_d = '{"Name" : "John", "Phone" : 765756657, "email" : "john@gmail.com"}'
dict_1 = json.loads(str_d)
print(dict_1, type(dict_1))
print("*"*50)
#string to set
str_j = "Python Programming"
set1 = set(str_j)
print(set1, type(set1))
