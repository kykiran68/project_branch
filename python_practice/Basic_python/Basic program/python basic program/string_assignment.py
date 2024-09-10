# question1
s1 = "IPL2024 CRICKET TROPHY"
first_char =s1[0]
last_char = s1[-1]
remaining_part = s1[1 : -1]
result = f"{last_char}{remaining_part}{first_char}"
print("result : ", result)

# question2
i = input("Enter sentence : ")
j = " "
k = 1
for k in range(len(i)):
    if k%2:
        j+=i[k]*2
    else:
        j+=i[k]
print(j)

# question 3
s2 = "GOOD MORNING"
first_char =s2[0]
last_char = s2[-1]
remaining_part = s2[-2: 0 : -1]
result = f"{last_char*2}{remaining_part}{first_char*2}"
print("result : ", result)

# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
char1 = input("Enter a string : ")
if len(char1)>2:
    char2 = char1[:2]+char1[-2:]
    print(char2)
else:
    print(" ")

# 2). Python string program that takes a list of strings and returns the length of the longest string.
char1 = input("Enter a string : ").split(",")
temp = 0
for char2 in char1:
    char3 = len(char2)
    if temp <char3:
        temp = char3
print(temp)

# 3). Python string program to get a string made of 4 copies of the last two characters
# of a specified string (length must be at least 2).
char1 = input("Enter a string : ")
index = 0
if len(char1) > 2:
    index = char1[-2:]
print(index*4)


# 4). Python string program to reverse a string if it’s length is a multiple of 4
char1 = input("Enter a string : ")
if len(char1)%4 == 0:
    print(char1[::-1])
else:
    print(char1)

# 5). Python string program to count occurrences of a substring in a string.
char1 = input("Enter a string : ")
#print(char1.count(input("enter substring ")))
char2=input("enter a substring: ")
count=0
i=0
while i<=len(char1)-len(char2):
    if char1[i:i+len(char2)]==char2:
        count+=1
    i+=1
print(count)

# 6). Python string program to test whether a passed letter is a vowel or consonant.
char1 = input("Enter a string : ")
#char2 ="0"
for char2 in char1:
    if "a"<=char2<="z" or "A"<=char2<="Z":
        #print("It is alphabet")
        if char2 in "AEIOU" or char2 in "aeiou":
            print("It is vowel",char2)
        else:
            print("It is consonent",char2)
    else:
        print("Invalid string = ",char2)


# 7). Find the longest and smallest word in the input string.
str2 = input("Enter a string : ")
l1 = str2.split(" ")
s_len = len(l1[0])
s_word = l1[0]
l_len=len(l1[0])
l_word=l1[0]
for word in l1:
    word_len = len(word)
    if word_len < s_len:
        s_len = word_len
        s_word = word
        print("smallest length :", s_len)
        print("smallest word :", s_word)
    if word_len > l_len:
        l_len = word_len
        l_word = word
        print("largest length :", l_len)
        print("largest word :", l_word)


# 8). Print most simultaneously repeated characters in the input string.
str_1 = input("Enter a string : ")
str_2 = " "
most_count = 0
most_digit = 0
counter = 1
for word in range(len(str_1)-1):
    if str_1[word] == str_1[word+1]:
        counter = counter+1
        if most_count<counter:
            most_count= counter
            str_2 = str_1[word]
    else:
        counter =1
print(str_2, most_count)


# 9). Write a Python program to calculate the length of a string with loop logic.
char1=input("Enter a string : ")
count = 0
for i in char1:
    count = count+1
print(count)


 # 10). Write a Python program to replace the second occurrence of any char with the special character $.
char1 = input("Enter the string :")
char2 = ""
for i in char1:
    if i in char2:
        char2+="$"
    else:
        #print(str1,end="")
        char2 = char2+i
print(char2)

# 11). Write a python program to get to swap the last character of a given string.
char1=input("Enter a string : ")
firstchar = char1[0]
lastchar = char1[-1]
remainchar = char1[1:-1]
result = f"{lastchar}{remainchar}{firstchar}"
print(result)


# 12). Write a python program to exchange the first and last character of each word from the given string.
char1 = input("Enter your string : ")
list1 = char1.split(" ")
char2 = ""
for i in list1:
    if len(i) > 1:
        list2 = i[-1] + i[1:-1] + i[0]
        char2 = char2 + " " + list2

    else:
        print(i)
print("Updated string : ", char2)


# 13). Write a python to count vowels from each word in the given string show as dictionary output.
char1 = input("Enter your string : ")
l1 = char1.split(" ")
dict11=dict()
for j in l1:
    count = 0
    for i in j:
        if i in "AEIOUaeiou":
            count = count+1
        dict11[j]=count
print(dict11)


# 14). Write a python to repeat vowels 3 times and consonants 2 times.
num = input("Enter a number: ")
result =""
digit = 0
for digit in num:
    if "a"<=digit<="z" or "A"<=digit<="Z":
        if digit in "AEIOUaeiou":
            result = digit*3
        else:
            result = digit*2
    print(result,end="")


# 15). Write a python program to re-arrange the string
s1 = input("Enter a string :")
l1 = s1.split(" ")
l1.reverse()
print(" ".join(l1))


# 16). Write a python program to get all the digits from the given string.
s1 = input("Enter your string : ")
l1 = s1.split(" ")
for i in l1:
    if i.isnumeric():
        print("digit is . ",i)


# 17). Write a python program to replace the words “Java” with “Python” in the given string.
s1 = "JAVA is the Best Programming Language in the Market"
s1 = s1.replace("JAVA", "Python")
print(s1)


# 18). Write a Python program to get all the palindrome words from the string.
s1 = input("Enter a string ")
l1 = s1.split(" ")
print(s1)
for word in l1:
    if word==word[::-1]:
        print("It is palindrome : ",word)

# 19). Write a Python program to create a string with a given list of words.
l1 = input("Enter the string in list formet : ").split(",")
l2 =list(l1)
print("given list is : ",l2)
l3=" ".join(l2)
print("The new stringis : ",l3)


# 20). Write a Python program to remove duplicate words from the string.
s1 = input("Enter a string : ")
l1 = s1.split(" ")
l2 = []
for value in l1:
    if value not in l2:
        l2.append(value)
print(" ".join(l2))


#21 Write a Python to remove unwanted characters from the given string.
s1 = input("Enter your string : ")
for word in s1:
    if word.isalpha():
        i = " ".join(word)
        print(i,end="")


# 22). Write a Python program to find the longest capital letter word from the string.
str_1 = input("Enter a string : ")
str_2 = str_1.split(" ")
str_empty = " "
for word in str_2:
    if word.isupper() and len(str_empty)<len(word):
        str_empty=word
        print("Longest capital letter word: ",str_empty)
        break
    else:
        print("No Capital letter word : ",str_1)
        break


# 23). Write a Python program to get common words from strings.
input1 = input("enter your first string : ").split(" ")
input2 = input("enter your second string : ").split(" ")
same_str = []
for i in input1:
    for j in input2:
        if i == j:
            same_str.append(i)

print(" ".join(same_str))



# 24). Write a Python program to find the smallest and largest word in a given string.
str1=input("Enter a sentance : ").split()
small_str1=str1[0]
large_str1=str1[0]
for i in str1:
    if len(i)<len(small_str1):
        small_str1=i
    elif len(i)>len(large_str1):
        large_str1=i
print("Small : ",small_str1)
print("large : ",large_str1)


# 25). Check whether the given string is a palindrome (similar) or not.
input1 = input("enter your first string : ")

if input1 == input1[::-1]:
    print("It is palindrome : ",input1)
else:
    print("not a palindrome")


# 26). Write a program using python to reverse the words in a string.
l1 = input("Enter your string : ")
for word in l1:
    l2=(l1[::-1])
print(l2)

l1 = input("Enter your string : ")
l2 = l1.split(" ")
print(" ".join(l2[::-1]))


# 27). Write a program to calculate the length of a string.
l1 = input("Enter your string : ")
count = 0
for word in l1:
    count+=1
print(count)


# 28). Write a program to calculate the frequency of each character in a string.
l2 = list(input("Enter your string : ").split())
dict1 ={}
for word in l2:
    for i in word:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i] = 1
print(dict1)


# 29). Write a program to combine two strings into one.
str1 =input("enter your first string : ")
str2 = input("Enter your second string : ")
print(str1+str2)


# 30). Write a program to print characters at even places in a string.
str1 ='We are reading python'  #str1 =input("Enter your input : ")
output = ""
for i in range (len(str1)):
    if i%2 != 0:
        output+=str1[i]
print(output)

# 31). Write a program to check if a string has a number or not.
string = "python1"
count = 0
for char in string:
    if char.isnumeric():
        count += 1
if count > 0:
    print(True)
else:
    print(False)


# 32). Write a python program to count the number of vowels in a string.
s1 = input("Enter your string :")
count = 0
for char in s1:
    if char in 'aeiouAEIOU':
        count+=1
print(count)


# 33). Write a python program to count the number of consonants in a string.
s1 = input("Enter your string :")
count = 0
for char in s1:
    if char not in 'aeiouAEIOU' and 'a'<char<'z':
        count+=1
print(count)


# 34). Write a program to print characters at odd places in a string.
s1 = input("Enter your string :")
for char in range(len(s1)):
    if char%2 !=0:
        print(s1[char],end="")


# 35). Write a program to remove all duplicate characters from a given string in python.
s1 = input("Enter your string :")
output = ''
for char in s1:
    if char not in output:
        output+=char
print(output)


# 36). Write a program to check if a string has a special character or not
s1 = input("Enter your string :")
count = 0
for char in s1:
    if char.isalnum():
        count = 0

    else:
        count += 1
if count > 0:
    print("It contain special character")
else:
    print("It has no special character")


# 37). Write a program to exchange the first and last letters of the string
s1 = input("Enter your string :")
f_let = s1[0]
l_let = s1[-1]
output = f'{l_let}{s1[1:-1]}{f_let}'
print(output)


# 38). Write a program to convert all the characters in a string to Upper Case.
s1 = input("Enter your string :").upper()
print(s1)


# 39). Write a program to remove a new line from a string using python.
str1=("enter\n")
print(str1.rstrip())

# 40). Write a python program to split and join a string
str1 = input("Enter you string : ")
str2 = str1.split(" ")
print(str2)
str3 = "-".join(str2)
print(str3)


# 41). Write a program to print floating numbers up to 3 decimal places and convert it to string.
str1 = float(input("Enter you string : "))
str2 = " "
str2+= str(round(str1,3))
print(str2)


# 43). Write a python program to find the location of a word in a string
str1 = input("Enter yout string : ").split(" ")
str2 = input("Enter word to find : ")
if str2 in str1:
    print(str1.index(str2))

str1 = list(input("Enter yout string : ").split(" "))
str2 = input("Enter word to find : ")
print(str1.index(str2))

# 44). Write a program to count occurrences of a word in a string.
str1 =  input("Enter your string : ").split(" ")
str2 = input("Enter word to find : ")
print(str1.count(str2))


# 45). Write a python program to find the least frequent character in a string.


# 46). Find the words greater than the given length.
input1 = input('Enter a string : ')
l1 = input1.split(' ')
length = int(input('Enter the length : '))
for word in l1:
    if len(word) > length:
        print(word)


#  47). Write a program to get the first 4 characters of a string.
input1 = input('Enter a string : ')
print(input1[:5])


# 48). Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
input1 = input('Enter a string : ')
a = input1[:2]
b = input1[-2:]
print(a+b)


# 49). Write a python program to print the mirror image of the string.
input1 = input('Enter a string : ')
print(input1[::-1])


# 50). Write a python program to split strings on vowels
input1 = input('Enter a string : ')
for word in input1:
    if word in "AEIOUaeiou":
        k=input1.replace(word," ")
print(k)


# 51). Write a python program to replace multiple words with certain words.
string = "I’m learning python at Sqatools"
List = string.split(" ")

for i in range(len(List)):
    if List[i] == "python":
        List[i] = "SQA"
    elif List[i] == "Sqatools":
        List[i] = "TOOLS"

print(" ".join(List))


# 52). Write a python program to replace different characters in the string at once.
string = "Sqatool python"
new_str = ""
for char in string:
    if char == "a":
        new_str += "1"
    elif char == "t":
        new_str += "2"
    elif char == "o":
        new_str += "3"
    else:
        new_str += char
print(new_str)


# 53). Write a python program to remove empty spaces from a list of strings.
string = "Sqatool   python"
str1 = list(string)
list1 = []
for word in str1:
    if word != " ":
        i = "".join(word)
        print(str(i),end="")



# 54).  Write a python program to remove punctuations from a string
input1 = 'Sqatools :@#$%^&*( is best, for python '
str1 = ""
for word in input1:
    if word.isalnum() or word ==" ":
        str1+=word
print(str1)


# 55).  Write a python program to find duplicate characters in a string
str1=input("Enter a string : ")
list1=[]
for word in str1:
    if str1.count(word)>1:
        list1.append(word)
print(set(list1))


# 56).  Write a python program to check whether the string is a subset of another string or not
str1 = (input("Enter a string : "))
str2 = (input("Enter a sub string : "))
str3 = set(str1)
count = 0
for i in str3:
    if i in str2:
        count += 1
    else:
        count = 1
if count == len(str2):
    print(True)
else:
    print(False)


# 57). Write a python program to sort a string
str1="".join(sorted(input("Enter a string : ")))
print(str1)


# 59). Write a python program to check if the substring is present in the string or not
str1 = input("Enter a string : ").split(" ")
str2 = input("Enter a sub string : ").split(" ")
count = 0
for word in str2:
    if word in str1:
        count += 1
    else:
        count = 1
if count == len(str2):
    print(True)
else:
    print(False)


# 60). Write a program to find all substring frequencies in a string.
str1 = "abab"
test = []

for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        test.append(str1[i:j])

dict1 = dict()
for val in test:
    dict1[val] = test.count(val)

#Printing output
print(dict1)


# 61). Write a python program to print the index of the character in a string.
s1=input("Enter a string : ")
str1 = list(s1)
str2 = input("Enter a string : ")

print(str1.index(str2))


# 62). Write a program to strip spaces from a string.
i ='    sqaltoolspythonfun     '
print(i.strip())


# 63). Write a program to check whether a string contains all letters of the alphabet or not.
input1 = input("Enter a string : ").lower()
if sorted(input1) == list('abcdefghijklmnopqrstuvwxyz'):
    print(True)
else:
    print(False)


# 64). Write a python program to convert a string into a list of words.
s1=input("Enter a string : ").split(' ')
print(s1)


# 65). Write a python program to swap commas and dots in a string.
string = "sqa,tools.python"

a=string.replace(",",".")
print(a)


# 66). Write a python program to count and display the vowels in a string
string = input("enter a string : ")
count = 0
l1 = []
for word in string:
    if word in 'AEIOUaeiou':
        count+=1
        l1.append(word)
print(l1)
print(count)


# 67). Write a Python program to split a string on the last occurrence of the delimiter.
string = 'we are reading'
print(string.rsplit("i",2))


# 68). Write a Python program to find the first repeated word in a given string.
string = input("enter a string : ").split(" ")
output = [ ]
count = 0
for word in string:
    if word in output:
        print(word)
        break
    else:
        output.append(word)



# 70). Write a Python program to remove spaces from a given string.
string = input("enter a string : ").split()
a="".join(string)
print(a)


# 71). Write a Python program to capitalize the first and last letters of each word of a given string.
string = input("enter a string : ").split()
for word in string:
    l = word[0].upper()
    u = word[-1].upper()
    a = f"{l}{word[1:-1]}{u}"
    print(a,end=" ")


# 72). Write a Python program to calculate the sum of digits of a given string.
string = input("enter a string : ")
out = 0
for word in string:
    if word.isnumeric() :
        out += int(word)
print(out)


# 73). Write a Python program to remove zeros from an IP address.
put = '289.03.02.054 '

for digit in put:
    if digit != '0':
        print(digit,end="")


# 74). Write a program to find the maximum length of consecutive 0’s in a given binary string using python.
input1 = '100001001000000010'
max_len = 0
current_len = 0
for i in input1:
    if i== '0':
        current_len +=1
        max_len = max(max_len,current_len)
    else:
        current_len= 0
print(max_len)

# 75). Write a program to remove all consecutive duplicates of a given string using python.
put = 'xxxxyyzzxxrrxr'
output=''
for val in range(len(put)-1):
    if put[val] !=put[val+1]:
        output+=put[val]
output+=put[-1]
print(output,end="")


# 76). Write a program to create strings from a given string.
# Create a string that consists of multi-time occurring characters in the said string using python.
input_string = "hello worldh"
multi_time_chars = ""
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char] = 1
for char,count in char_count.items():
    if count>1:
        multi_time_chars+=char
print(multi_time_chars)


# 77). Write a Python program to create a string from two given
# strings combining uncommon characters of the said strings.
str1 = "123456"
str2 = "567810"
output1 =''
output2 =''
for word in str1:
    if word not in str2:
        output1+=word
for word1 in str2:
    if word1 not in str1:
        output2+=word1
print(output1+output2)


# 78). Write a Python code to remove all characters except the given character in a string.
input1 = set(input("Enteer a string : "))
input2 = set(input("Enter a letter to check : "))
output =""
for word in input1:
    if word in input2:
        output+=word
print(output)


# 79). Write a program to count all the Uppercase, Lowercase, special character
# and numeric values in a given string using python.
input1 = input("Enteer a string : ")
int_cnt = 0
upp_cnt = 0
l_cnt = 0
s_char = 0
for word in input1:
    if word.isnumeric():
        int_cnt+=1
    elif word.islower():
        l_cnt+=1
    elif word.isupper():
        upp_cnt+=1
    else:
        s_char+=1
print("The count of number is : ", int_cnt)
print("The count of uppercase is : ", upp_cnt)
print("The count of lower case is : ", l_cnt)
print("The count of special character is : ", s_char)


# 80). Write a Python program to count a number of non-empty substrings of a given string.
str1 = "sqatools12"

result = int(len(str1) * (len(str1) + 1) / 2)

#Printing output
print(result)


# 81). Write a program to remove unwanted characters from a given string using python.
input1 = input("Enteer a string : ")
for word in input1:
    if word.isalnum():
        print(word,end='')


# 83). Write a program to extract numbers from a given string using python.
input1 = input("Enteer a string : ").split()
for word in input1:
    if word.isnumeric():
        print(word,end='')


# 84). Write a program to split a given multiline string into a list of lines using python.
put ='''This string Contains\nMultiple\nLines'''
print(put.split('\n'))


# 85). Write a program to add two strings as they are numbers using python.
str1 = '6'
str2 = '4'
print(int(str1)+int(str2))


# 86). Write a program to extract name from a given email address using python.




# 87). Write a  program that counts the number of leap years within the range of years using python.
# The range of years should be accepted as a string.
int1 = int(input("Enter a starting range : "))
int2 = int(input("Enter a ending range : "))
count1 = 0
for num in range(int1, int2 + 1):
    if num % 100 == 0:
        if num % 400 == 0:
            count1 += 1
    else:
        if num % 4 == 0:
            count1 += 1

print(count1)


# 88). Write a program to insert space before every capital letter appears in a given word using python.
input1 = 'SqaTools pyThon'
result =""
for word in input1:
    if word.isupper():
        result+=" "+word
    else:
        result+=word
print(result)


# 89). Write a program to uppercase half string using python.
input1 = 'SqaToolspyThon'
length = len(input1)
output = ''
for word in range(length//2):
    a =input1[word].lower()
    output+=a
for word in range(length//2,length):
    a = input1[word].upper()
    output+=a
print(output)


# 90). Write a program to split and join a string using “-“.
input1 = input("Enter a string : ").split(' ')
print(input1)
a = "_".join(input1)
print(a)


# 92). Write a program to avoid spaces in string and get the total length
input1 = 'sqatools is best for learning python'.split()
a = "".join(input1)
length = len(a)
print(length)


# 93). Write a program to accept a string that contains only vowels
str1 = input("Enter a string : ")
count = 0
List = ["a","e","i","o","u","A",
       "E","I","o","U"]

for char in str1:
    if char in List:
        count += 1

if count == len(str1):
    print("Accepted")
else:
    print("Not Accepted")


# 94). Write a program to remove the kth element from the string
str1 = "sqatools"
print(str1[:2]+str1[3:])


# 95). Write a program to check if a given string is binary or not.
# Hint: Binary numbers only contain 0 or 1.
str1 = input("Enter a string : ")
out =0
for num in str1:
    if num =="0" or num =='1':
        out+=1
    else:
        out = 1
if out ==len(str1):
    print("It is binary number")
else:
    print("It is not binary")


# 96). Write a program to add ‘ing’ at the end of the string using python.
str1 = input("Enter a string : ")
str2 ="ing"
print(str1+str2)


# 97). Write a program to add ly at the end of the string if the given string ends with ing.
str1 = input("Enter a string : ")
if str1[-3:]=='ing':
    print(str1+'ly')
else:
    print(str1)


# 98). Write a program to reverse words in a string using python.
str1 = input("Enter a string : ").split()
print(str1[::-1])


# 99). Write a program to print the index of each character in a string.
str1 = input("Enter a string : ")
for word in str1:
    print(word, str1.index(word))


# 100). Write a program to find the first repeated character in a string and its index.
str1 = input("Enter email address: ")
index = str1.index("@")
str2 = ""
for char in str1[:index]:
    if char.isalpha():
        str2 += char
print(str2)



# 101). Write a program to swap cases of a given string using python.
str1 = input("Enter a string : ")
print(str1.swapcase())


# 102). Write a program to remove repeated characters in a string and replace it with a single letter using python.
str1 = input("Enter a string : ")
print("".join(set(str1)))


# 103). Write a program to print a string 3 times using python.
str1 = input("Enter a string : ")
print(str1*3)


# 104). Write a program to print each character on a new line using python.
str1 = input("Enter a string : ")
for char in str1:
    print(char, end="\n")


# 105). Write a program to get all the email id’s from given string using python.
input1 = ("We have some employee whos john@gmail.com email ids are randomly "
          "distributed jay@liccom we want to get hari@facebook.com"
          " all the email mery@hotmail.com ids from this given string.").split()
for word in input1:
    if '@' in word:
        print(word)


# 106). Write a program to get a list of all the mobile numbers from the given string using python.
input1 = ('We have 2233 some employee 8988858683 whos 3455 mobile numbers '
          'are randomly distributed 2312245566 we want 453452 to get 4532892234 '
          'all the mobile numbers 9999234355  from this given string.').split()
for word in input1:
    if word.isnumeric() and len(word) == 10:
        print(word)

