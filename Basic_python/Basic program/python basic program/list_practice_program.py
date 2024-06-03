list_1 = [4,18,"a", 3.5, [5,7,8],(1,2,3),True,{"a":123, "b":456},{6,2,8,4}]
print(list_1[5])
print(list_1[7]["b"])
print(list_1[-4][1])
print(list_1[-1])
for val in list_1:
    print(val, end=" ")
for i in range(len(list_1)):
    print(i, list_1)
    break
# Add data to list
list_1.append("Hello")
print(list_1)
# Inserting data to list
list_1.insert(1, "b")
print(list_1)
# extend the list
lista = ["a","b","c","d"]
listb = [1, 2, 3, 4]
listb.extend(lista)
print(listb)

# list concatanation
listc = lista + listb
print(listc)

# remove data from list
listc.remove("b")
print(listc)

# remove data using pop method
listd = listc.pop(4)
print(listd,listc)

# removing data using clear method
listc.clear()
print(listc)

# delete variable from memory
del listc

# replace data in list
l1 = [4, 11, 7, 88, 23, 15]
l1[2] = 500
print(l1)
l1[1:4] = ["a", 8, "c"]
print(l1)

# count method
l2 = [3,6,8,2,6,8,[8,2]]
print(l2.count(8))


# index method in list
print(l2.index(8))
# sort method in list
listk= [4,1,5,2,8,11,7]
listk.sort()
print(listk)
listk.sort(reverse=True)
print(listk)

# sorted()function
listm = [4,6,77,11,34,2,5,7]
result = sorted(listm)
print(result)

result2 = sorted(listm,reverse=True)
print(result2)


# reverse method
l5 = [2,6,9,45,61,99,43]
l5.reverse()
print(l5)

# reverse function
l6 = [2,6,9,45,61,99,43]
data = reversed(l6)
print(data)
for val in data:
    print(val,end=" ")


# shallow copy in list
listp = [4,7,2,8,1,33]
listq = listp
listr = listq
listr.append(100)
listq.append(200)
print(listp)
print(listq)
print(listr)

# deep copy
listx = [4,7,2,8,1,33]
listy = listx.copy()
listz = listy.copy()
listy.append(30)
listz.append(40)
print(listx)
print(listy)
print(listz)


list11 = [5,7,33,44,11,2,6,9]
print(max(list11))
print(min(list11))
print(sum(list11))

# list comprehension
# program which is divisible 3 or 7
result1 = [x for x in list11]
print(result1)
result1 = [x for x in list11 if x%3==0 or x%7==0]
print(result1)

# print list in given manner in even and odd form
for value in list11:
    if value%2 ==0:
        result1.append((value,'even'))
    else:
        result1.append((value,'odd'))
print(result1)


#from list comprenhesion
result5 = [(val,'even') if val%2==0 else(val,'odd') for val in list11]
print(result5)

# program to find duplicate value from list and remove it
listk = [2,6,1,2,5,9,8,5,7]
duplicate = []
result =[]
for value in listk:
    if value not in result:
        result.append(value)
    else:
        duplicate.append(value)
print(result)
print(duplicate)


# program to move all positive value in RHS and negative value in LHS.
listi = [4,8,-1,-6,0,-4,10]
negative =[]
positive=[]
for digit in listi:
    if digit<0:
        negative.append(digit)
    else:
        positive.append(digit)
print(negative + positive)


# 1). Python program to calculate the square of each number from the given list.
lista = input("Enter the list : ")
listb = lista.split(",")
result =0
digit =[]
for i in listb:
    if i.isnumeric():
        a = int(i)**2
        digit.append(a)
    else:
        digit.append(i)
print(digit)

# 2). Python program to combine two lists.
lista = list(input("Enter the list : ").split(" "))
listb = list(input("Enter second list : ").split(" "))
listc = lista + listb
print(listc)

# 3). Python program to calculate the sum of all elements from a list.
lista = input("Enter the list : ")
listb = lista.split(",")
result = 0
digit = []
for i in listb:
    if i.isnumeric():
        result = result + int(i)

    else:
        digit.append(i)
digit.append(result)

print(digit)

# 4). Python program to find a product of all elements from a given list.

lista = ("Enter the list : ")
listb = lista.split(",")
result = 1
digit = []
for i in listb:
    if i.isnumeric():
        result = result * int(i)

    else:
        digit.append(i)
digit.append(result)
print(digit)

# 5). Python program to find the minimum and maximum elements from the list.
lista = input("Enter the list : ")
listb = lista.split(",")
for i in listb:
    if i.isnumeric():
        i = listb
print("largest number is ",max(i))
print("Smallest number is ",min(i))

# 6). Python program to differentiate even and odd elements from the given list.
lista = input("Enter the list : ")
listb = lista.split(",")
output =[]
for i in listb:
    if int(i)%2 == 0:
        output.append((i,"even"))
    else:
        output.append((i,"odd"))
print(output)


# 7). Python program to remove all duplicate elements from the list.
lista = input("Enter the list : ")
listb = lista.split(",")
duplicate =[]
output =[]
for i in listb:
    if i not in output:
        output.append(i)
    else:
        duplicate.append(i)
print(output)
print(duplicate)


# 8). Python program to print a combination of 2 elements from the list whose sum is 10.
lista = input("Enter the list : ")
listb = lista.split(",")
output =[]
for i in range(len(listb)):

   for j in range(i+1, len(listb)):

       if listb[i] + listb[j] ==10:

           print(listb[i], listb[j])


# 9). Python program to print squares of all even numbers in a list.
lista = input("Enter the list : ")
listb = lista.split(",")
output =[]
for i in listb:
    if i.isnumeric():
        if int(i)%2 ==0:
            i =int(i)
            output.append(i**2)
        else:
            output.append(i)
    else:
        output.append(i)
print(output)


# 10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
lista = input("Enter the list : ")
listb = lista.split(",")
odd =[]
even = []
for i in listb:
    if i.isnumeric():
        if int(i)%2 ==0:
            even.append(i)
        else:
            odd.append(i)
    else:
        pass
print(odd+even)


# 11).  Python program to get common elements from two lists.
lista = input("Enter the list : ")
stra = lista.split(",")
listb = input("Enter the list : ")
strb = listb.split(",")
result = []
for val1 in stra:

    if val1 in strb:
        result.append(val1)
print(result)


# 12). Python program to reverse a list with for loop.
lista = input("Enter the list : ")
stra = lista.split(",")
for i in range(len(stra)-1,-1,-1):
    print(stra[i], end=" ")


# 13). Python program to reverse a list with a while loop.
lista = input("Enter the list : ")
stra = lista.split(",")
i = 0
while i<=len(stra):
    i = i-1
    print(stra[i], end=" ")


# 14). Python program to reverse a list using index slicing.
lista = input("Enter the list : ")
stra = lista.split(",")
print(stra[::-1])


# 15). Python program to reverse a list with reversed and reverse methods.
lista = input("Enter the list : ")
stra = lista.split(",")
stra.reverse()
print(stra)

data = reversed(stra)
for val in data:
    print(val,end=" ")


# 16). Python program to copy or clone one list to another list.
lista = input("Enter the list : ")
listb = input("Enter the list : ")
stra = lista.split(",")
strb = listb.split(",")
stra.extend(strb)
print(stra)


# 17). Python program to return True if two lists have any common member.
lista = input("Enter the list : ")
listb = input("Enter the list : ")
stra = lista.split(",")
strb = listb.split(",")
for val1 in stra:
    if val1 in strb:
        Result=True
        break
    else:
        Result=False
print(Result)


# 18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
lista = input("Enter a list : ")
stra = lista.split(",")
output =[]
for i in range(len(stra)):
    if i!=1 and i!=3 and i !=6:
        output.append(stra[i])
print(output,end=" ")


# 19). Python program to remove negative values from the list.
lista = input("Enter a list : ")
stra = lista.split(",")
output =[]
for val in stra:
    if int(val) >=0:
        output.append(val)
    else:
        pass
print(output)


# 20). Python program to get a list of all elements which are divided by 3 and 7.
lista = input("Enter a list : ")
stra = lista.split(",")
output =[]
for val in stra:
    if int(val)%3 ==0 or int(val)%7==0:
        output.append(val)
    else:
        pass
print(output)


# 21). Python program to check whether the given list is palindrome or not.
lista = input("Enter a list : ")
stra = lista.split(",")
output =[]
if stra == stra[::-1]:
    output.append(stra[::-1])
    print("It is palindrome : ",output)
else:
    print("Not a palendrome : ",stra)


# 22). Python Program to get a list of words which has vowels in the given string.
lista = input("Enter a list : ")
stra = lista.split(",")
output = []
for value in stra:
    for vowel in value:
        if vowel in "aeiouAEIOU" and value not in output:
            output.append(value)

        else:
            pass
print(output)


# 23). Python program to add 2 lists with extend method.
lista = input("Enter the list : ")
stra = lista.split(",")
listb = input("Enter the list : ")
strb = listb.split(",")
stra.extend(strb)
print(stra)


# 24). Python program to sort list data, with the sort and sorted method.
stra = [1,4,9,100,69,6,70]
result = sorted(stra)
print(result)

stra = [3,6,9,4,67,100,80,5,76]
stra.sort()
print(stra)


# 25). Python program to remove data from the list from a specific index using the pop method.
lista = input("Enter the list : ")
stra = lista.split(",")
val=stra.pop(3)
print(stra,val)


# 26). Python program to get the max, min, and sum of the list using in-built functions.
list11 = [5,7,33,44,11,2,6,9]
print(max(list11))
print(min(list11))
print(sum(list11))


# 27). Python program to check whether a list contains a sublist.
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [4,5]
check=0
for i in l1:
    for j in l2 :
        if i == j:
            check+=1
if check==len(l2):
    print("The list contain sublist")
else:
    print("Invalid sub list")

l1 = list(input("enter list : ").split(","))
l2 = list(input("enter sub list : ").split(","))
check=0
for i in l1:
    for j in l2 :
        if i == j:
            check+=1
if check==len(l2):
    print("The list contain sublist")
else:
    print("Invalid sub list")


# 28). Python program to generate all sublists with 5 or more elements in it from the given list.






# 29). Python program to find the second largest number from the list.
l1 = list(input("enter list : ").split(","))
l1.sort()
print("2nd largest no.",l1[-2])


# 30). Python program to find the second smallest number from the list.
l1 = list(input("enter list : ").split(","))
l1.sort()
print("2nd smallest no.",l1[1])


# 31). Python program to merge all elements of the list in a single entity using a special character.
l1=list(input("Enter a sentance : ").split(","))
l2 = "@".join(l1)
print(l2)


# 32). Python program to get the difference between two lists.

l1 = [21,45,67,90]
l2 = [21]
for i in l1:
    if i not in l2:
        print(i,end = " ")


# 33). Python program to reverse each element of the list.
num = list(input("Enter a list : ").split(" "))
lista = []
for i in num:
    j=i[::-1]
    lista.append(j)
print(lista)


# 34). Python program to combine two list elements as a sublist in a list.
list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
out =[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if i == j:
            a = [list1[i],list2[j]]
            out.append(a)
print(out)

list1 = list(input("Enter first list : ").split(" "))
list2 = list(input("Enter second list : ").split(" "))
out =[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if i == j:
            a = [list1[i],list2[j]]
            out.append(a)
print(out)


# 35). Python program to get keys and values from the list of dictionaries.
i1 = [{'a':12}, {'b': 34}, {'c': 23}, {'d': 11}, {'e': 15}]
l1 =[]
l2 = []
for val in i1:
    for k,v in val.items():
        l1.append(k)
        l2.append(v)
print(l1)
print(l2)


# 37). Python program to convert a string into a list.
str1 = input("Enter a string : ").split(',')
l1 = list(str1)
print(l1)


# 38). Python program to replace the last and the first number of the list with the word.
input1 = [12, 32, 33, 5, 4, 7]
input1[0] = 'sqa'
input1[-1] = "tool"
print(input1)


# 39). Python program to check whether the given element is exist in the list or not.
input1= [12, 32, 33, 5, 4, 7]
s = str(input1)
print(s)
i = input("enter value : ")
if i in s:
    print("it is present in list")
else:
    print("It is not present in list")


# 40). Python program to remove all odd index elements.
input1= [12, 32, 33, 5, 4, 7, 33]
v =[]
for l in range(len(input1)):
    if l%2 == 0:
        v=input1[l]
        print(v)


# 41). Python program to take two lists and return true if then at least one common member.
#Input list
list1 = [25,65,77,14,23,96]
list2 = [65,35,62,77]

#Creating result variable
result = False

for val in list1:
    for ele in list2:
        if ele == val:
            result = True
            print(f"{ele} exists in list2", result)


# 42). Python program to convert multiple numbers from a list into a single number.
list1 = list(input("Enter a list : ").split())
for val in list1:
    print(val,end="")


# 43). Python program to convert words of a list into a single string.
list1 = ['Sqa', 'Tools', 'Best', 'Learning', 'Platform']
str1 =''
for word in list1:
    str1+=word
print(str1)


# 44). Python program to print elements of the list separately.
list1 = [('Black', 'Yellow', 'Blue'), (50, 55, 60), (30.0, 50.5, 55.66)]
for word in list1:
    print(word)


# 45). Python program to create a sublist of numbers and their squares from 1 to 10.
l =[]
for i in range(1,11):
    list1=[i,i**2]
    l.append(list1)
print(l,end=" ")


# 46). Python program to create a list of five consecutive numbers in the list.
l = []
for i in range(4):
    list1 =[]
    for j in range(1,6):
        list1.append(5*i+j)
    l.append(list1)
print(l)

# 47). Python program to insert a given string at the beginning of all items in a list.
l =['1', '2', '3', '4', '5']
l1 =[]
str1 = 'sqa'
for i in l:
    s=str1+i
    l1.append(s)
print(l1)


# 48). Python program to iterate over two lists simultaneously and create a list of sublists.
list1 = [1, 3, 5, 7, 9]
list2 = [8, 6, 4, 2, 10]
list3 =[]
for val,ele in zip(list1,list2):
    l = [val,ele]
    list3.append(l)
print(list3)


# 49). Python program to move all positive numbers on the left side and negative numbers on the right side.
list1 = [2, -4, 6, 44, -7, 8, -1, -10]
pos =[]
neg =[]
for digit in list1:
    if int(digit)>0:
        pos.append(digit)
    else:
        neg.append(digit)
    a = pos+neg
print(a)


# 50). Python program to move all zero digits to the end of a given list of numbers.
list1 =  [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
pos =[]
zero =[]
for digit in list1:
    if int(digit) > 0:
        pos.append(digit)
    else:
        zero.append(digit)
a = pos+zero
print(a)


# 51). Python program to find the list in a list of lists whose sum of elements is the highest.
#Input list
list1 = [[11, 2, 3], [4, 15, 2], [10, 11, 12], [7, 8, 19]]

#Printing output
print(max(list1,key=sum))


# 52). Python program to find the items that start with a specific character from a given list.
list1 =  ['abbcd', 'ppq', 'abdd', 'agr', 'bhr', 'sqqa', 'tools', 'bgr']
a =[]
b =[]
s =[]
for word in list1:
    if word[0] == 'a':
        a.append(word)
    elif word[0] == 'b':
        b.append(word)
    elif word[0] == 's':
        s.append(word)
print("The word statr with a is : ", a)
print("The word statr with b is : ", b)
print("The word statr with s is : ", s)


# 54). Python program to remove consecutive duplicates of given lists.
list1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
a = set(list1)
print(a)


# 55). Python program to pack consecutive duplicates of given list elements into sublists.
#Input list
original_list = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]

packed_list = []  # Initialize the packed list
current_sublist = []  # Initialize the current sublist

for item in original_list:
    if not current_sublist or item == current_sublist[-1]:
        # If the current sublist is empty or the current item is equal to the last item in the sublist
        current_sublist.append(item)  # Add the item to the current sublist
    else:
        packed_list.append(current_sublist)  # Add the current sublist to the packed list
        current_sublist = [item]  # Start a new sublist with the current item

if current_sublist:
    packed_list.append(current_sublist)  # Add the last sublist to the packed list if it's not empty

print("Packed list:", packed_list)


# 56). Python program to split a given list into two parts where the length of the first part of the list is given.
list1 = [4, 6, 7, 3, 2, 5, 6, 7, 6, 4]
l =[]
l.append(list1[:4])
l.append(list1[4:])
print(l)


# 57). Python program to insert items at a specific position in the list.
l = [2, 4, 6, 8, 3, 22]
l.insert(3,55)
print(l)


# 59). Python program to create a 3*3 grid with numbers.
l =[]
for word in range(3):
    l.append([])
    for ele in range(4,7):
        l[word] = l.append(ele)
print(l)


# 60). Python program to zip two lists of lists into a list.
l1 = [[1, 3], [5, 7], [9, 11]]
l2 = [[2, 4], [6, 8], [10, 12, 14]]
list3 = list(zip(l1,l2))
print(list3)



# 61). Python program to convert the first and last letter of each item from Upper case and lowercase.
l1 = ['Learn', 'python', 'From', 'Sqa', 'tools']
list1 =[]
list2 =[]
for word in l1:
    a = f"{word[0].upper()}{word[1:-1]}{word[-1].upper()}"
    list1.append(a)
    b = f"{word[0].lower()}{word[1:-1]}{word[-1].lower()}"
    list2.append(b)
print(list1)
print(list2)



# 62). Python to find maximum and minimum values in the given heterogeneous list.
#Input list
list1 = ["Sqa", 6, 5, 2, "Tools"]

#Finding min and max
max_ = max(value for value in list1 if isinstance(value, int))
min_ = min(value for value in list1 if isinstance(value, int))

#Printing output
print("Maximun: ", max_)
print("Minimun: ", min_)


# 63). Python program to sort a given list in ascending order according to the sum of its sublist.
list1 = [[3, 5, 6], [2, 1, 3], [5, 1, 1], [1, 2, 1], [0, 4, 1]]
print(sorted(list1,key=sum))



# 64). Python program to extract the specified sizes of strings from a given list of string values.
input1 = list(input("Enter your list : ").split())
input2 = int(input("Enter the length of word : "))
l1 =[]
for word in input1:
    if len(word) == input2:
        l1.append(word)
print(l1)


# 65). Python program to find the difference between consecutive numbers in a given list.
input1 = [1, 1, 3, 4, 4, 5, 6, 7]
l =[]
for i in range(len(input1) -1):
    num =  input1[i+1] - input1[i]
    l.append(num)
print(l)



# 66). Python program to calculate the average of the given list.
input1 = list(input("Enter the numbers to find average : ").split(","))
sum1 =0
length = len(input1)
for word in input1:
    sum1 +=int(word)
    avg = sum1/length
print(avg)


# 67). Python program to count integers in a given mixed list.
input1 = ['Hello', 45, 'sqa',  23, 5, 'Tools', 20]
l =[]
c =0
for word in input1:
    if isinstance(word,int):
        l.append(word)
        c+=1
print(l)
print(c)



# 68). Python program to access multiple elements of the specified index from a given list.
input1 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
l =[]
a =input1[2],input1[3],input1[5],input1[6]
l.append(a)
print(l)



# 69). Python program to check whether a specified list is sorted or not.
input1 = list(input("Enter your list : ").split(","))
if input1==sorted(input1):
    print(True)
else:
    print(False)


# 70). Python program to remove duplicate dictionaries from a given list.
input1 = [{'name': 'john'}, {'city': 'mumbai'}, {'Python': 'laguage'}, {'name': 'kir'}]
l1 =[]
for key in input1:
    if key not in l1:
        l1.append(key)
print(l1)



# 71). Python program to check if the elements of a given list are unique or not.
list1 = [2, 5, 6, 7, 4, 11, 2, 4, 66, 21, 22, 3]

for i in range(len(list1)):
    if list1[i] not in list1[i+1:]:
        print("True")
        break
    else:
        print("False")
        break



# 72). Python program to remove duplicate sublists from the list
input1 = [[1, 2], [3, 5], [1, 2], [6, 7]]
l1 =[]
for num in input1:
    if num not in l1:
        l1.append(num)
print(l1)



# 73). Python program to create a list by taking an alternate item from the list.
input1 = [3, 5, 7, 8, 2, 9, 3, 5, 11]
l1 = []
'''
for i in range(len(input1)):
    if i%2 ==0:
        l1.append(input1[i])
print(l1)
'''
for i in range(0, len(input1), 2):
    l1.append(input1[i])
print(l1)



# 74). Python program to remove duplicate tuples from the list.
input1 = [(2, 3), (4, 6), (5, 1), (2, 3), (7, 9), (5, 1)]
input2 =[]
for value in input1:
    if value not in input2:
        input2.append(value)
print(input2)



# 75). Python program to insert an element before each element of a list.
input1 = [3, 5, 7, 8]
l1 =[]
for i in input1:
    l1.append(('a',i))
print(l1)


# 76). Python program to remove the duplicate string from the list.
input1 = ['python', 'is', 'a', 'best', 'language', 'python', 'best']
l1 = []
for word in input1:
    if word not in l1:
        l1.append(word)
print(l1)


# 77). Python program to get the factorial of each item in the list.
num = int(input("Enter the number for factorial : "))
l1 = []
j = 1
for i in range(1, num + 1):
    j = j * i
    l1.append(j)

print(l1)
# 78). Python program to get a list of Fibonacci numbers from 1 to 20.
l =[]
j = 0
k=1
for i in range(1,21):
    l.append(j)
    m=j+k
    j=k
    k=m
print(l)



# 79). Python program to reverse all the numbers in a given list.
num =  [123, 145, 633, 654, 254]
l1 = []
for word in num:
    ans=0
    while word>0:
        rem = word%10
        ans = ans*10 + rem
        word = word//10
    l1.append(ans)
print(l1)



# 80). Python program to get palindrome numbers from a given list.
num =  [121, 134, 354, 383, 892, 232]

l1 = []
for word in num:
    w = word
    ans=0
    while word>0:
        rem = word%10
        ans = ans*10 + rem
        word = word//10
    if w == ans:
        l1.append(ans)
print(l1)



# 81). Python program to get a count of vowels in the given list.
l =['Learning', 'Python', 'From', 'SqaTool']
count = 0
for word in l:
    for ele in word:
        if ele in "AEIOUaeiou":
            count+=1
print(count)


# 82). Python program to get the list of prime numbers in a given list.
l1 =[11, 8, 7, 19, 12, 29]
l2 =[]
for num in l1:
    count =0
    for i in range(1,num):
        if num%i == 0:
            count+=1
    if count==1:
        l2.append(num)
print(l2)



# 83). Python program to get a list with n elements removed from the left and right.
l1 =[2, 5, 7, 9, 3, 4]
l2 = (l1[2:])
l3 = (l1[:-1])
l1.remove(4)
print(l1)
print(l2)
print(l3)



# 84). Python program to create a dictionary with two lists.
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [234, 123, 456, 343, 223]
d = dict(zip(list1,list2))
print(d)


# 85). Python program to remove the duplicate item from the list using set.
list1 = [2, 5, 7, 8, 2, 3, 4, 12, 5, 6]
list2 = set(list1)
print(list2)


# 86). Python program to insert a sublist into the list at a specific index.
list1 = [4, 6, 8, 2, 3, 5]
list1.insert(3,[4,5,6])
print(list1)


# 87). Python program to calculate the bill per fruit purchased from a given fruits list.
#Input lists
list1 = [["apple", 30], ["mango", 50], ["banana", 20], ["lichi", 50]]
list2 = [["apple", 2],["mango",10]]

for value in list1:
    for var in list2:
        if value[0] == var[0]:
        #Printing output
            print("Fruit: ", value[0])
            print("Bill: ", value[1]*var[1])


# 88). Python program to calculate percentage from a given mark list, the max mark for each item is 100.
list1 = [80, 50, 70, 90, 95]
length = len(list1)
add = 0
for val in list1:
    add+=int(val)
    pcent = add/(length*100)*100
print(pcent)



# 89). Python program to get the list of all palindrome strings from the given list.
list1 = ['data', 'python', 'oko', 'test', 'ete']
l =[]
for word in list1:
    if word == word[::-1]:
        l.append(word)
print(l)


# 90). Python program to flatten a given nested list structure.






# 91). Python program to convert tuples in the list into a sublist.
list1 = [(3, 5), (6, 8), (8, 11), (12, 14), (17, 23)]
l = []
for val in list1:
    val = list(val)
    l.append(val)
print(l)


# 92). Python program to create a dictionary from a sublist in a given list.
list1 = [['a', 5], ['b', 8], ['c', 11], ['d', 14], ['e', 23]]
d = dict(list1)
print(d)


# 93). Python program to replace ‘Java’ with ‘Python’ from the given list.
list1 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
l = []
for word in list1:
    if word == 'Python':
        word = 'JAVA'
    l.append(word)
print(l)


# 94). Python program to convert the 3rd character of each word to a capital case from the given
list1 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
l = []
for word in list1:
    if len(word)>3:
        a = f"{word[:3]}{word[3].upper()}{word[4:]}"
    else:
        a = word
    l.append(a)
print(l)



# 95). Python program to remove the 2nd character of each word from a given list.
list1 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
l = []
for word in list1:
    if len(word)>3:
        a = f"{word[:2]}{word[3:]}"
    else:
        a = word
    l.append(a)
print(l)


# 96). Python program to get a length of each word and add it as a dictionary from the given list.
list1 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
l = {}
d =[]
for word in list1:
    l[word] = len(word)
d.append(l)
print(d)


# 97). Python program to remove duplicate dictionaries from the given list.
list1 = [{'Hello': 5, 'student': 7, 'are': 3, 'learning': 8, 'Python': 6, 'Its': 3, 'Language': 8}]
d={}
l =[]
for word in list1:
    for key,val in word.items():
        if key not in d:
            d[key] = val
l.append(d)
print(l)


# 99). Python program to round every number in a given list of numbers and print the total sum of the list.
#Input list
list1 = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
list2 = []

for value in list1:
    list2.append(round(value))

#Printing output
total = (sum(list2))
print(total)



# 100).  Python Program to get the Median of all the elements from the list.
list1 = [4, 45, 23, 21, 22, 12, 2,4,21,22]
output =[]
a = sorted(list1)
print(a)
l = len(a)
if l%2 ==0:
    m =a[l//2]+a[(l//2)-1]
    med = m/2
    output.append(med)
else:
    output.append(a[l//2])
print(output)


#








