char = 0
str1=""
f = open("read_loop_file","r")
data = f.read()
for i in data:
    if i.isalnum():
        pass
    else:
        char+=1
        str1+=i
f.close()
print(char)
print(str1)
