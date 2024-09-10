# 1). Python tuple program to create a tuple with 2 lists of data.
s1 = input("Enter a string : ")
l1 = s1.split(",")
s2 = input("Enter second string : ")
l2 = s2.split(",")
output = ( )
for i in range(len(l1)):
    for j in range(len(l2)):
        if i==j:
            output+=tuple(l1[i])+tuple(l2[j])
print(output)

# 2). Python tuple program to find the maximum value from a tuple.
s1 = tuple(input("Enter a string : "))
#s1 = (5,9,4,3)
print(max(s1))

# 3). Python tuple program to find the minimum value from a tuple.
s1 = tuple(input("Enter a string : ").split(","))
#s1 = (5,9,4,3)
print(min(s1))

# 4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
s1 = [1,2,3,4,5]
s2 = [1,4,9,16,25]
print(tuple(zip(s1,s2)))

tup3 = input("Enter a string : ").split(",")
l1 =[]
l2 =[]
for num in tup3:
    l1.append(int(num))
for num in l1:
    l3 = num**2
    l2.append((num,l3))
print(l2)


# 5). Python tuple program to create a tuple with different datatypes.
f = float(input("Enter a float value"))
i = int(input("Enter a integer"))
b = bool(input("Enter a boolean value"))
s = input("Enter a string")
l = list(input("Enter list"))
t = tuple(input("Enter a tuple"))
k={'I':5,'j':4}
d = (f,i,b,s,l,t,k)
print(d)


# 6). Python tuple program to create a tuple and find an element from it by its index no.
tup1 = tuple(input("Enter a tuple : "))
#tup1 = (2,6,9,"kiran",[1,2,3],{'a':1, 'b':2})
print(tup1[:])

#7). Python tuple program to assign values of tuples to several variables and print them.
a,b,c=int(input("enter a number : ")),int(input("enter a number : ")),int(input("enter a number : "))
print("a,",a)
print("b,",b)
print("c,",c)

# 8). Python tuple program to add an item to a tuple.
tup1= ( 18, 65, 3, 45)
tup2 = (15,)
print(tup1 + tup2)

# 9). Python tuple program to convert a tuple into a string.
tup1= ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
l1 = list(tup1)
str1="".join(l1)
print(str1)

str1= tuple(input("Enter a string : ").split(","))
l1 = list(str1)
str2="".join(l1)
print(str2)

# 10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
str1= tuple(input("Enter a string : ").split(","))
print(str1[1],str1[-3])


# 11). Python tuple program to check whether an element exists in a tuple or not.
tup1 = ( 'p' ,"y", "t", "h", "o", "n")
if "k" in tup1:
    print(True)
else:
    print(False)

str1= tuple(input("Enter a string : "))
val = input("Enter input : ")
if val in str1:
    print(True)
else:
    print(False)


# 12). Python tuple program to add a list in the tuple.
tup1 = (2,5,8,6)
list1 = [1,2,3]
list2 = tuple(list1)
tup1 = tup1 + list2
print(tup1)

tup1 = tuple(input("Enter a tuple : ").split(","))
list1 = list(input("Enter a list : ").split(","))
list2 = tuple(list1)
tup1 = tup1 + list2
print(tup1)

# 13). Python tuple program to find sum of elements in a tuple.
tup = (1,2,3,4,5,6,7,8,9)
print(sum(tup))


#  15). Python tuple program to create a tuple having squares of the elements from the list.

t = [(1, 5, 7), (3, 6)]
s = []
for i in t:
    for j in i:
        s.append(j ** 2)
print(tuple(s))
#-------------------------or---------------------------
t = tuple(input("enter tuple : ").split(","))
s=[]
for i in t:
    s.append(int(i)**2)
print(tuple(s))


# 16). Python tuple program to multiply adjacent elements of a tuple.
in1 = (1,4,3,9)
input1 = list(in1)
output = []
for i in range(len(input1)-1):
    output.append((input1[i]*input1[i+1]))
print(output)


# 17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.


# 18). Python tuple program to convert a list into a tuple and multiply each element by 2.
input1 = [12,65,34,77]
t = []
for i in input1:
    t.append(i**2)
print(tuple(t))

# 19). Python tuple program to remove an item from a tuple
input1=('p','y','t','h','o','n')
l1 = list(input1)
l1.pop()
print(tuple(l1))


# 20). Python tuple program to slice a tuple.
num =tuple(input("Enter your tuple : ").split(","))
print(num[1:4])
print(num[0:7])


# 21). Python tuple program to find an index of an element in a tuple.
A=('s','q','a','t','o','o','l','s')
b = A.index('a')
print(b)


# 22). Python tuple program to find the length of a tuple.
A=('v','i','r','a','t')
l = len(A)
print(l)


# 23). Python tuple program to convert a tuple into a dictionary.
A=((5,'s'),(6,'l'))
B = dict(A)
print(B)


# 24). Python tuple program to reverse a tuple.
a = ( 4, 6, 8, 3, 1)
b = a[::-1]
print(b)


# 25). Python tuple program to convert a list of tuples in a dictionary.



# 26). Python tuple program to pair all combinations of 2 tuples.
l = []
a =(2,3)
b =(5,6)
for i in a:
    for j in b:
        l.append((i,j))
for i in a:
    for j in b:
        l.append((j,i))
print(l)



# 27). Python tuple program to remove tuples of length i.
a = [ (2, 5, 7), (3, 4), ( 8, 9, 0, 5) ]
a.pop(1)
print(a)


# 28). Python tuple program to remove tuples from the List having an element as None.
a = [(None, 2), (None, None), (5, 4), (1,6,7)]
l =[]
for val in a:
    if None not in val:
        l.append(val)
print(l)



# 29). Python tuple program to remove Tuples from the List having every element as None.
input1 = [(None,), (None, None), (5, 4), (1,6,7),(None,1)]
l =[]
for val in input1:
    if not all(i == None for i in val):
        l.append(val)
print(l)




# 30). Python tuple program to sort a list of tuples by the first item.
i = [ (1, 5), (7, 8), (4, 0), (3, 6) ]
a=sorted(i,key=lambda tup:tup[0])
print(a)


# 31). Python tuple program to sort a list of tuples by the second item.
i = [ (1, 5), (7, 8), (4, 0), (3, 6) ]
a=sorted(i,key=lambda tup:tup[1])
print(a)



# 32). Python tuple program to sort a list of tuples by the length of the tuple.
i = [ (1, 5), (7, 8), (4, 0), (3, 6) ]
a=sorted(i,key=lambda tup:len(tup))
print(a)


# 33). Python tuple program to calculate the frequency of elements in a tuple.
i = ('a', 'b', 'c', 'd', 'b', 'a', 'b')
d = {}
for val in i:
    if val in d:
        d[val] += 1

    if val not in d:
        d[val] = 1
print(d)


# 34). Python tuple program to filter out tuples that have more than 3 elements.
i = [ (1, 4), (4, 5, 6), (2, ), (7, 6, 8, 9), (3, 5, 6, 0, 1) ]
l1 = []
for word in i:
    if len(word)>3:
        l1.append(word)
print(l1)


# 35). Python tuple program to assign the frequency of tuples to each tuple.
i = [ ('s','q'), ('t', 'o', 'o', 'l'), ('p', 'y'), ('s', 'q') ]
d = {}
for word in i:
    if word in d:
        d[word] +=1
    else:
        d[word] =1
print(d)



# 36). Python program to find values of tuples at ith index number.
input1 = [ (1, 2, 3), (6, 5, 4), (7, 6, 8), (9, 0, 1) ]
print(input1[3])



# 37). Python tuple program to test whether a tuple is distinct or not.
input1 = (3,4,5,4,6,3)
if len(set(input1))==len(input1):
    print("It is unique tuple ")
else:
    print("It us not unique")



# 38). Python tuple program to convert a tuple to string datatype.
input1 = (4,1,7,5)
d = str(input1)
print(d)



# 39). Python tuple program to remove empty tuples from a list of tuples.
input1 = [("",), ('a', 'b'), ('c', 'd', 'e'), ('d'), ()]
i = []
for val in input1:
    if len(val) != 0:
        i.append(val)
print(i)



# 40). Python tuple program to sort a tuple by its float element.
input1 = [(3,5.6),(6,2.3),(1,1.8)]
a = sorted(input1, key =lambda x : float(x[1]))
print(a)



# 41). Python tuple program to count the elements in a list if an element is a tuple.
input1 = [1,6,8,5,(4,6,8,0),5,4]
count =0
for i in input1:
    if type(i) == tuple:
        count= len(i)
print(count)



# 42). Python tuple program to multiply all the elements in a tuple.
input1 = (5,4,3,1)
t = 1
for word in input1:
    if type(word) == int:
        t*=word
print(t)


# 43). Python tuple program to convert a string into a tuple.
input1 = 'Sqatools'
tup = tuple(input1)
print(tup)


# 44). Python tuple program to convert a tuple of string values to a tuple of integer values.
input1 = ( '4563', '68', '1', )
tup = []
for num in input1:
    if type(num) == str:
        tup.append(int(num))
print(tuple(tup))



# 45). Python tuple program to convert a given tuple of integers into a number.
tup = (4,5,3,8)
str1 = ""
print("Original tuple: ",tup)
for val in tup:
    str1 += str(val)
num = int(str1)
print("Integer: ",num)


# 46). Python tuple program to compute the element-wise sum of tuples.
a = (1, 6, 7)
b = (4, 3, 0)
c = (2, 6, 8)
s = tuple(map(sum,zip(a,b,c)))
print(s)


# 47). Python tuple program to convert a given list of tuples to a list of lists.
a = [(1,5),(7,8),(4,0)]
l = []
for ele in a:
    l.append(list(ele))
print(l)


# 48). Python tuple program to find all the tuples that are divisible by a number.
l = [(10,5,15),(25,6,35),(20,10)]
print("Original list of tuples: ",l)
for tup in l:
    count = 0
    for ele in tup:
        if ele%5 == 0:
            count += 1
    if count == len(tup):
        print("\nTuple in which all elements are divisible by 5: \n",tup)



# 49). Python tuple program to find tuples having negative elements.
a = [ (1, -7), (-4, -5), (0, 6), (-1, 3) ]
l =[]
for word in a:
    for i in word:
        if i<0 :
            l.append(word)
            break
print(l)


# 50). Python tuple program to find the tuples with positive elements.
a = [(1, 7), (-4, -5), (0, 6), (-1, 3)]
l = []
for word in a:
    if all(i >= 0 for i in word):
        l.append(word)

print(l)


# 51). Python tuple program to remove duplicates from a tuple.
a = (6, 4, 9, 0, 2, 6, 1, 3, 4)
b = set(a)
print(tuple(b))


# 52). Python tuple program to extract digits from a list of tuples.
a = [ (6, 87, 7), (4, 53), (11, 28, 3) ]
l = []
for ele in a:
    for word in ele:
        l.append(word)
print(l)



# 53). Python tuple program to multiply ith element from each tuple from a list of tuples.
a = [ (4, 8, 3), (3, 4, 0), (1, 6, 2) ]
i = 1
prod=1
for num in a:
    prod *=num[i]
print(prod)



# 54). Python tuple program to flatten a list of lists into a tuple.
a = [ ['s'], ['q'], ['a'], ['t'], ['o'], ['o'], ['l'], ['s'] ]
l =[]
for ele in a:
    for i in ele:
        l.append(i)
print(tuple(l))



# 55). Python tuple program to flatten a tuple list into a string.
a = [ ('s', 'q', 'a'), ('t', 'o'), ('o', 'l', 's') ]
s = ""
for word in a:
    for ele in word:
        s+=ele
print(s)



# 56). Python tuple program to convert a tuple into a list by adding the string after every element of the tuple.
a = (1, 2, 3, 4)
b='sqatools'
l = []
for word in a:
    l .append(word)
    l.append(b)
print(l)


# 57). Write a program to convert a tuple to tuple pair.
a = (4, 2, 3)
i = 0
list1 =[]
for num in a:
    if num!=a[0]:
        list1.append((a[i], num))
print(list1)



# 59). Python tuple program to convert a list of lists to a tuple of tuples.
a = [ ['sqatools'], ['is'], ['best']]
l = []
for word in a:
    l.append(tuple(word))
print(tuple(l))



# 60). Python tuple program to extract tuples that are symmetrical with others from a list of tuples.
l = [('a', 'b'), ('d', 'e'), ('b', 'a')]
print("Original list of tuples: ", l)

symmetric_tuples = []

for tup in l:
    if (tup[1], tup[0]) in l:
        symmetric_tuples.append(tup)

print("Tuples that are symmetric: ", symmetric_tuples)



# 62). Python tuple program to remove nested elements from a tuple.
text = ( 's', 'q', 'a', ('t', 'o', 'o', 'l', 's'), 'i', 's', 'b', 'e', 's', 't' )
l =[]
for ele in text:
    if type(ele) !=tuple:
        l.append(ele)
        out = tuple(l)
print(out)



# 63). Python tuple program to sort a tuple by the maximum value of a tuple.
text = [ (1, 5, 7), (3, 4, 2), (4, 9, 0) ]

a = sorted(text,key = lambda x : max(x), reverse = True)
print(a)


# 64). Python tuple program to sort a list of tuples by the minimum value of a tuple.
text = [ (1, 5, 7), (3, 4, 2), (4, 9, 0) ]

a = sorted(text,key = lambda x : min(x))
print(a)


# 65). Python tuple program to concatenate two tuples.
tup1 = ('s','q','a')
tup2 = ('t','o','o','l')
print(tup1+tup2)



# 66). Python tuple program to order tuples by external list.
a=[('very',8),('i',6),('am',5),('happy',0)]
list1=['i','am','very','happy']
output1=[]
for i in list1:
    for j in a:
        for k in j:
            if k ==i:
                output1.append(j)
print(output1)



# 67). Python tuple program to find common elements between two lists of tuples.
A=[(1,5),(4,8),(3,9)]
B=[(9,3),(5,6),(5,1),(0,4)]
c =[]
for ele in A:
    for word in B:
        if sorted(ele) == sorted(word):
            c.append(ele)
print(c)


# 68). Python tuple program to convert a binary tuple to an integer.
tup = (1, 1,0,0)
print("Original tuple is:", tup)

binary_string = ""
for val in tup:
    binary_string += format(val,'b')
print(binary_string)
decimal_number = int(binary_string, 2)

print("Decimal number:", decimal_number)


# 69). Python tuple program to count the total number of unique tuples.
tup = [ (8, 9), (4, 7), (3, 6), (8, 9) ]
count = 0
l1 = []
for val in tup:
    if val not in l1:
        count+=1
        l1.append(val)
print(l1)
print(count)



# 70). Python tuple program to calculate the average of the elements in the tuple.
tup = tuple(input("Enter your tuple : ").split(","))
output = 0
length = len(tup)
for num in tup:
    output += int(num)
    avg = output/length
print(avg)


# 71). Python tuple program to swap tuples.
A=(7,4,9)
B=(3,)
C=()
C=A
A=B
B=C
print(A)
print(B)



# 72). Python tuple program to check the type of the input and return True
# if the type is a tuple and False if it is not a tuple.
A=( 7, 4, 9, 2, 0 )
if type(A)==tuple:
    print(True)
else:
    print(False)



# 73). Python tuple program to find the last element of a tuple using negative indexing.
A=('p','y','t','h','o','n')
print("The the element of tuple is : ",A[-1])




