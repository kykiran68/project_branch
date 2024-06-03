"""
read mode(r)
write mode(w)
append mode(a)
"""

def read_file(filename):
    file = open(filename,'r')
    d=file.read()
    file.close()
    print(d)
read_file('E:\\read_data\\reading.txt')

def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()
write_file('writefile', "Add content to fresh file.")

# #1. write a python program Replace file content JAVA with PYTHON.

with open("read_file", "r") as input_file:

    content = input_file.read()

# Replace "JAVA" with "PYTHON" in the content
modified_content = content.replace("JAVA", "PYTHON")

# Open the output file in write mode
with open("writefile.txt", "w") as output_file:
    # Write the modified content to the output file
    output_file.write(modified_content)


#    #2. write a python program to get all the email id from given file.


# #3. Write a python program to get all the phone number from given file.'''
def mail_id(filename):

    mail = []
    number = []
    with open (filename, 'r') as file:
        data = file.read()
    word_list  = data.split()
    for word in word_list:
        if"@" in word:
            mail.append(word)
        if len(word)==10 and word.isnumeric():
            number.append(word)
    print(mail,number)
    return mail,number
mail,number = mail_id('output.txt')


def readfile_content(filename):
    with open(filename,'r') as file:
        data = file.read()
        print(data)
        print(file.closed)
    print(file.closed)
readfile_content('read_file')


# read specific number of character from file
def read_bytes(filename,bytecount):
    with open(filename,'r') as file:
        data = file.read(bytecount)
        print(data)
read_bytes('writefile',5)


# read n number of lins with readline method
def read_line(filename, lines):
    with open(filename, 'r') as file:
        for i in range(lines):
            data = file.readline()
        print(data,end="")
read_line('read_line.txt',6)


# read list of lines with help of readlines
def read_lines(filename):
    with open(filename, 'r') as file:
        lines_data = file.readlines()
        return lines_data
print(read_lines('read_line.txt'))


# program to combine two file with alternate line
def combine(file1,file2,file3):
    with open(file1,'r') as file1_obj:
        file1_list = file1_obj.readlines()
    with open(file2,'r') as file2_obj:
        file2_list = file2_obj.readlines()
    file3_list =[]
    len_list = 0
    if len(file1_list) > len(file2_list):
        len_list = len(file1_list)
    else:
        len_list = len(file2_list)
    for i in range(len_list):
        file3_list.append(file1_list[i])
        file3_list.append(file2_list[i])
    with open(file3, 'a') as file3_obj:
        for line in file3_list:
            file3_obj.write(line)
combine('file1', 'file2','file3')


# 1). Python Program How to read a file in reading mode.
def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    print(data)
read_file("writefile")


# 2). Python file program to overwrite the existing file content.
def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()
write_file("writefile", "This is new file added to the content menu")


# 3).  Python file program to append data to an existing file.
def append_file(filename, content):
    file = open(filename, "a")
    file.write(content)
    file.close()
append_file("writefile", "\n This is appended to the new file")


 #


