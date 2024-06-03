str1 = "python"
output ={}
for i in range(len(str1)):
    output[str1[i]] = i+1
print(output)
# {'p': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n': 6}
str1="PROGRAM"
lista=[1,2,3,4,5,6,7]
output={}
for i in range(len(lista)):
    for j in range(len(str1)):
        if j==i:
            output[lista[i]]=str1[j]*(i+1)
print(output)
#------------------------------OR----------------------------
str1=input("Enter a string : ")
lista=input("Enter a total length of string like 1,2,3,4,5,... : ").split(",")
output={}
for i in range(len(lista)):
    if len(str1)==len(lista):
        for j in range(len(str1)):
            if j==i:
                output[lista[i]]=str1[j]*(i+1)
    else:
        print("Invalid length of string ")
        break
print(output)


# 1). Python Dictionary program to add elements to the dictionary.
dict1 = {"a":1, "b":2, "c":3}
dict1["d"] = 4
print(dict1)

dict1 = input("Enter the key value : ").split(" ")
dict2 = input("Enter the value : ").split(" ")
dict3 = {}
for i in range(len(dict1)):
    dict3[dict1[i]] = dict2[i]

dict3["name"] = "kiran"
print(dict3)

# 2). Python Dictionary program to print the square of all values in a dictionary.
dict1 = input("Enter the key value : ").split(" ")
dict2 = input("Enter the value : ").split(" ")
dict3 = {}
dict4 = {}
for i in range(len(dict1)):
    dict4[dict1[i]] = dict2[i]
    c = int(dict2[i])**2
    dict3[dict1[i]] = c
print(dict4)
print(dict3)


# 3). Python Dictionary program to move items from dict1 to dict2.
p ={1:"chandan", 2:"pagal",3:"insan",4:"hai"}
dicta = {}
for i in p:
    dicta[i]=p[i]
p.clear()
print(p)
print(dicta)

# 4). Python Dictionary program to concatenate two dictionaries
dict1 = {'Name': "Harry", "Rollno":345, "Address":"Jordan"}
dict2 = {"Age" : 25, "salary": "$25k"}
dict1.update(dict2)
print(dict1)


# 5). Python Dictionary program to get a list of odd and even keys from the dictionary.
dict1 = {1: 25, 5:"abc", 8:"pqr", 21:"xyz", 12:"def", 2:"utv"}
even1={}
odd1={}
for k1,v1 in dict1.items():
    if k1%2 == 0:
        even1[k1]=v1
    else:
        odd1[k1]=v1
print("Even keys : ",even1)
print("Odd keys : ",odd1)


# 6). Python Dictionary Program to create a dictionary from two lists.
l1 = ["a", "b", "c", "d", "e"]
l2 = [12, 23, 24, 25, 15, 16]
dict1 = {}
for i in range(len(l1)):
    dict1[l1[i]]=l2[i]
print(dict1)


# 7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
l1 =[4, 5, 6, 2, 1, 7, 11]
d1 ={}
for i in range(len(l1)):
    if l1[i]%2 == 0:
        d1[l1[i]] = l1[i]**2
    else:
        d1[l1[i]] = l1[i]**3
print(d1)


# 8). Python Dictionary program to clear all items from the dictionary.
dict1 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}

dict1.clear()
print(dict1)


# 9). Python Dictionary program to remove duplicate values from Dictionary.
d1 = {"a":12, "b":2, "c": 12, "d": 5, "e": 35, "f": 5}
d2 = {}
for k,v in d1.items():
    if v not in d2.values():
        d2[k]=v
print(d2)


# 10). Python Dictionary program to create a dictionary from the string.
input1  = "SQATools"
count = 1
dict1 = {}
for val in input1:
    if val in dict1:
        count += 1
    else:
        count = 1
    dict1[val] = count
print(dict1)


# 11). Python Dictionary program to sort a dictionary using keys.
Inputk = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
for k in sorted(Inputk):
    print(k,":",Inputk[k])






# 13). Python Dictionary program to add a key in a dictionary.
input1 = {"d" : 21, "b" : 53,  "a": 13, "c": 41}
input1["e"] = 55
print(input1)

# 14). Python Dictionary program to concatenate two dictionaries.
d1 = {"name" : "yash", "city" :  "pune"}
d2 = {"course" : "python", "institute" : "sqatools"}
d1.update(d2)
print(d1)


# 15). Python Dictionary program to swap the values of the keys in the dictionary.
d1 = {"name" : "yash", "city" :  "pune"}
d2 = {}
for k,v in d1.items():
    d2[v] = k
print(d2)


# 16). Python Dictionary program to get the sum of all the items in a dictionary.
dict1 = {"x" : 23, "y" : 10 , "z" : 7}
total = 0
for val in dict1.values():
    total = total+val
print(total)


# 17). Python program to get the size of a dictionary in python.
# Hint : use sys.getsizeof(var) method.
import sys
input1 = {'name' : 'virat', 'sport' : 'cricket'}
print(str(sys.getsizeof(input1)))

# 18). Python Dictionary program to check whether a key exists in the dictionary or not.
dict1 = {'city': 'pune', 'state': 'maharashtra'}
count = 0
for k in dict1.keys():
    if k == "country":
        count += 1

if count > 0:
    print("key is there")
else:
    print("key not present")


# 19). Python program to iterate over a dictionary.
dict1 = {'food':'burger', 'type':'fast food'}
for k in dict1:
    print(k,":",dict1[k])


# 20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
l1 = [1,2,3,4,5,6]
dict1 = {}
for i in l1:
    dict1[i] = i**3
print(dict1)


# 21). Python Dictionary program to insert a key at the beginning of the dictionary.
input1 = { 'course' : 'python',  'institute' : 'sqatools' }
input2 = {'name':'omkar'}
input2.update(input1)
print(input2)


# 22). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
dict1 = [1,2,3,4,5]
dict2 = {}
for i in dict1:
    dict2[i] = i**2
print(dict2)



# 23). Python Dictionary program to find the product of all items in the dictionary.
d ={ 'a' : 2, 'b' : 4, 'c' : 5}
output = 1
for key,val in d.items():
    output*=val
print(output)



#  24). Python Dictionary program to remove a key from the dictionary.
d ={'a':2,'b':4,'c':5 }
d.pop('c')
print(d)



# 25). Python Dictionary program to map two lists into a dictionary.
a = [ 'name', 'sport', 'rank', 'age']
b = ['Virat', 'cricket', 1,  32]
d ={}
for val,ele in zip(a,b):
    d[val]=ele
print(d)


# 26). Python Dictionary program to find maximum and minimum values in a dictionary.
a = { 'a' : 10, 'b' : 44 , 'c' : 60, 'd' : 25}
l =[]
for val in a.values():
    l.append(val)
l.sort()
print(max(l))
print(min(l))



# 27). Python Dictionary program to group the same items into a dictionary value.
input1 =[1,3,4,4,2,5,3,1,5,5,2,]
a = sorted(input1)
d ={}
for val in a:
    if val in d:
        d[val].append(val)
    else:
        d[val]=[val]
print(d)


# 28). Python Dictionary program to replace words in a string using a dictionary.
string = 'learning python at sqa-tools'
Dict = {'at':'is','sqa-tools':'fun'}

for key, value in Dict.items():
    string = string.replace(key, value)

print(string)


# 29). Python Dictionary program to remove a word from the string if it is a key in a dictionary.
String = 'sqatools is best for learning python'
Dict = {'best':2,'learning':6}

str2 = ""
for word in String.split(" "):
    if word not in Dict:
        str2 += word + " "

print(str2)


# 30). Python Dictionary program to remove duplicate values from dictionary values.
dict1 = {'marks1':[23,28,23,69],'marks2':[ 25, 14, 25]}

for key,val in dict1.items():
    for ele in val:
        if ele in val:
            val.remove(ele)

print(dict1)



#


