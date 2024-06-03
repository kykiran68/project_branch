s = "welcome to the world of python programming"
char = 0
for word in s:
    if word.isalpha():
        char += 1
print("The count of character in string is : ",char)
a = s.split()
print("The count of word in string is : ", len(a))

