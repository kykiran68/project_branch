str1 = 'Hello'
str2 = "Python Programming"
str3 = '''
In common usage, data is a collection 
of discrete or continuous values that 
convey information, 654353 describing the 
quantity, quality, ###*#&*^* fact, statistics, 
other basic units of meaning, or 
'''

str4 = """
In common usage, data is a collection 
of discrete or continuous values that 
convey information, describing the 
"""

str5 = "Hello we are learning 'Python' Programing"
str6 = 'Hope you are "enjoying" the learning Process'

print(str1, type(str1))
print("_" * 50)

print(str2, type(str2))
print("_" * 50)

print(str3, type(str3))
print("_" * 50)

print(str4, type(str4))
print("_" * 50)

print(str5, type(str5))
print("_" * 50)

print(str6, type(str6))
print("_" * 50)

# Ways to do the string formatting
Name = 'Rohan'
Age = 30
City = "Bangalore"
# My name is john and age is 25 and I am living in Mumbai


# 1. String concatenation
result = "My name is " + Name + " and age is " + str(Age) + " and I am living in " + City
print(result)

# 2. Format method
result2 = "My name is {} and age is {} and I am living in {}".format(Name, Age, City)
print(result2)

# F string formation
result3 = f"My name is {Name} and age is {Age} and I am living in {City}"
print(result3)

str1 = "Python"
# 0  1  2  3  4  5   +ve indexing
# P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1   -ve indexing

print(str1[1])  # y
print(str1[-5])  # y

print(str1[-2])  # o

# Get length of the given string

print("length of the string :", len(str1))  # 6

# Apply loop on the string

# without indexing
stra = "Python Learning"
for char in stra:
    print(char, end=" ")

print()
# with indexing
for i in range(len(stra)):
    # print(i, stra[i])
    print(stra[i], end=" ")

print()
print("_" * 40)
######################### String Slicing #######################
# Rule1 : str1[initial index : last index]
# It will return the substring, which includes the initials index value and exclude last index value

str_b = "Good Morning"
print("str_b[1:6] =", str_b[1:6])  # ood M

print("str_b[0:4] =", str_b[0:4])  # Good

print(str_b[2:-2])  # od Morni

print(str_b[-5:-1])  # rnin

print(str_b[-7: 10])  # Morni

print(str_b[-7:2])  # blank output

print(str_b[2:-7])  # od

#######################
print("_" * 50)
### Rule2 str1[:last index]
# in this rule default initial index is zero and last index will be the position we have defined.

str1 = "IPL 2024 Mumbai Indian"
print(str1[: 5])  # IPL 2
print(str1[: -7])  # IPL 2024 Mumbai

#################
# Rule3 : str[initial index : ]
# in this rule the default last index will be end of the string
str2 = "India is great country"
print(str2[2:])  # dia is great country
print(str2[-5:])  # untry

###########
# Rule4 : str1[initial index : last index : difference of index]
# In this rule initial index value will be included and last index value will excluded.

strc = "Good MorningH"

print(strc[2:8:1])  # od Mor

print(strc[2: 13: 2])  # o onnH

print(strc[-1:-6:-1])  # Hgnin

print(strc[-1:2:-1])  # HgninroM d

###################
print("_" * 50)
# Rule5 str1[:last index:different index value]
# by default initial index is zero if the difference is positive
# by default initial index is -1 if the difference is negative


str_d = "Learning Python"

# default initial index is zero
print(str_d[:8:1])  # Learning

# default initial index is -1
print(str_d[:8:-1])  # nohtyP

print(str_d[:2:-2])  # nhy nn

##################
# Rule6 : str[::difference value]
# the default initial index will be zero and last index will end of the string if difference is positive
# The default initial index will be -1 and last index will be begining of string if difference is negative

str_e = "Very Good Evening"

# the default initial index will be zero and last index will end of the string if difference is positive
print(str_e[::1])  # Very Good Evening
print(str_e[::2])  # Vr odEeig

# The default initial index will be -1 and last index will be begining of string if difference is negative
print(str_e[::-1])  # gninevE dooG yreV
# str_e[-1:-len(str)-1: -1]

print(str_e[::-2])  # gieEdo rV

########################################################

# Practice Assingment

# replace first char with last char
str1 = "IPL 2024 Cricket Trophy"
fist_char = str1[0]
last_char = str1[-1]
remaining_part = str1[1:-1]
# result = f"{last_char}{remaining_part}{fist_char}"
result = f"{str1[-1]}{str1[1:-1]}{str1[0]}"
print("Result :", result)  # yPL 2024 Cricket TrophI

# question2:  Repeat every second character 2 times in the given string
str1 = "Python"
# output = "pyythhonn"

# question3 :
str2 = "Good Morning"
# output = "ggninroM dooGG"

########################### String Methods #############
print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode',
 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
 'isprintable', 'isspace', 'istitle', 'isupper', 
 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'removeprefix', 'removesuffix', 
 'replace', 'rfind', 'rindex', 'rjust', 
 'rpartition', 'rsplit', 'rstrip', 'split', 
 'splitlines', 'startswith', 'strip', 'swapcase', 
 'title', 'translate', 'upper', 'zfill'

"""

# lower() method: this method convert all the characters in the lower case.
stra = "Python PrograMMing Is Fun"
print(stra.lower())  # python programming is fun

# upper() method :
print(stra.upper())  # PYTHON PROGRAMMING IS FUN

# islower() method : check given string is lower or not
str_b = "Hello"
str_c = "PYTHON"
str_d = "learning"

print(str_b.islower())  # False
print(str_d.islower())  # True

# isupper method : This method check given string in upper or not
print(str_b.isupper())  # False
print(str_c.isupper())  # True

# swapcase method : This method convert all upper case to lower and lower case to upper.
str_e = "We Learning Python Programming"
print(str_e.swapcase())  # wE lEARNING pYTHON pROGRAMMING

# title method : This method convert the given sentence in the title case, it means first
#                character of each word should be capital

str_f = "ipl 2024 india premier league"
print(str_f.title())  # Ipl 2024 India Premier League

# istitle() method : This method check given string is title case or not.
str_g = "We Learning Python Programming"
str_h = "We LeaRning pyThon ProGraMming"
print("Is title method :", str_g.istitle())  # True
print("Is title method :", str_h.istitle())  # False

# count method: This method return count any given sub string/char in given string.
str_g = "We Learning Python Programming"
print("count of P :", str_g.count("P"))  # 2
print("count of ing :", str_g.count("ing"))  # 2
print("count of n :", str_g.count("n"))  # 4

# index() method : This method return the index of any sub-string/char in the target string
str_g = "We Learning Python Programming"
print(str_g.index("L"))  # 3
print("index of ing:", str_g.index("ing"))  # 8
# print("index of M :", str_g.index("M")) # ValueError: substring not found


# find method:  This method find the sub-string/char in the target and string
#                if it is available, then it will return index of substring else it will return -1

str_h = "Python Programming"
print("find p:", str_h.find('p'))  # -1 # it means its not available
print("find r:", str_h.find("r"))  # 8

##############
# split method: This method split the target string from given delimeter and return the list of substrings

str_k = "Today is sunny day"
result = str_k.split(" ")
print("Result :", result)  # ['Today', 'is', 'sunny', 'day']

str_l = "I,am,working,as,software,engineer"
word_list = str_l.split(",")
print(word_list) # ['I', 'am', 'working', 'as', 'software', 'engineer']

print(str_k.split("i"))  # ['Today ', 's sunny day']

url = "https://www.google.com"
protcol = url.split(":")[1]
print("protocol :", protcol)  # https
print("domain :", url.split(".")[2])  # com
print("server :", url.split(".")[1])  # google
print(url.split("//")[1].split(".")[0])  # www

###########
# replace method: This method replace the one word from another from given string.
str_z = "Python Programming Language"
result = str_z.replace("Python", "Java").replace("Programming", "System") # Java Programming Language
print("result:", result )

print("_"*50)
###########
# strip method : This method remove all the trailing space from given string.
str3 = "  Python Programming  "

print(str3)
print(str3.strip())

# remove left side space, then we can use lstrip method
print(str3.lstrip())

# remove right side space, then we can user rstrip method
print(str3.rstrip())

print(str3.replace(" ", "-")) # --Python-Programming--

##################
# join method : This method join all the character of the string with any combination

str_v = "Programming"

result = "-".join(str_v)
print(result) # P-r-o-g-r-a-m-m-i-n-g

result2 = "&%T&*#$".join(str_v)
print("result2 :", result2) # P&%T&*#$r&%T&*#$o&%T&*#$g&%T&*#$r&%T&*#$a&%T&*#$m&%T&*#$m&%T&*#$i&%T&*#$n&%T&*#$g

result3 = result2.replace("&%T&*#$", "")
print("result3 :", result3) # Programming

# apply join method for list of values
list1 = ["Hello", "How", "Are", "you?"] #  Hello How Are you?
result4 = " ".join(list1)
print("result4 :", result4)

# apply join method for tuple
tup1 = ('8', '4', '5', '2', '67', '1', '7', '12')
result5 = "".join(tup1)
print("result5:", result5)


#############
# isnumeric() # This method check given string only contains numbers
str11 = "54646565"
print(str11.isnumeric())  # True

str12 = "5445345 22343"
print(str12.isnumeric())  # False


# isalnum(): This method check, for combination of alphabate and numbers
str13 = "Hello2345"
print("islanum str13:", str13.isalnum()) # True

# isalpha() : This method check for only alphabates
str14 = "Python"
print("isalpha :", str14.isalpha()) # True

# isspace() :  This method check for space in the given string.
str15 = " "
print(str15.isspace())  # True


# Write a python program to get mobile numbers and email ids from given string ##########
print("_"*40)
str15 = """
Search safer online 2333 with McAfee® S
ecure 434 Search powered by Yahoo. Color 
coded search testuser@facebook.com 5465465465 results tell you which 
sites 9898789789 are safe – and test@gmail.com which could be 
dangerous. McAfee® Secure Search updates 
your default admin@yahoo.com search provider 8768768756 in Chrome to 
help you stay protected.
"""

word_list = str15.split()
for word in word_list:
    if word.isnumeric() and len(word) == 10:
        print("Mobile Number :", word)
    elif "@" in word:
        print("email :", word)








