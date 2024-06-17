"""
read mode(r)
write mode(w)
append mode(a)
"""

def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    print(data)

#read_file("read_data.txt")
#read_file("E:\\Filesdata\\file1.txt")


def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()


# when we open file to write there are possible case.
# 1. write existing available file : It will update existing content of the file
# write_file("write_data.txt", "Good Morning")

# 2. write to new file. : It will create new file and add content.
# write_file("write_new_file.txt", "Add content to fresh file.")

#write_file("E:\\Filesdata\\write_new_file.txt", "Add content to fresh file.")

def append_file(filename, content):
    file = open(filename, "a")
    file.write(content)
    print("file is closed :", file.closed) # False
    file.close()
    print("file is closed :", file.closed) # True

# append existing file
#append_file("append_read_data.txt", "\nNew text content for test")

# append new file
#append_file("append_new_data.txt", "\nWorking on file handling concept")

######### Context Manager ###############

def read_file_with_context_manager(filename):
    with open(filename, "r") as file_obj:
        data = file_obj.read()
        print(data)
        print("file is closed :", file_obj.closed)  # False

    print("file is closed :", file_obj.closed) # True

#read_file_with_context_manager("read_data.txt")

####### Different read option of the file ########

# 1. read specific number of character from file

def read_number_of_byte(filename, byte_count):
    with open(filename, "r") as file_obj:
        data = file_obj.read(byte_count)
        print(data)

#read_number_of_byte("read_data.txt", 20)

# 2. Read n number of line with readline method.

def read_number_of_lines(filename, lines):
    with open(filename, "r") as file_obj:
        for i in range(lines):
            data = file_obj.readline()
            print(data, end="")

#read_number_of_lines("read_data.txt", 5)

# 3. read list of lines with help of readlines

def read_list_of_lines(filename):
    with open(filename, "r") as file:
        lines_data = file.readlines()
        return lines_data

#print(read_list_of_lines("read_data.txt"))
# ['1.You can run git rebase --abort\n', '2.to completely undo the rebase.\n', "3.Git will return you to your branch's\n", '4.state as it was before git rebase was\n', '5.called. You can run git rebase --skip\n', '6.to completely skip the commit. That means\n', '7.that none of the changes introduced by the\n', '8.problematic commit will be included.\n']


def read_specific_line(filename, line_no):
    lines_list = read_list_of_lines(filename)
    print(lines_list[line_no-1])

#read_specific_line("read_data.txt", 5)
# 5.called. You can run git rebase --skip
#read_specific_line("read_data.txt", 2)
# 2.to completely undo the rebase.

def print_specific_number_line_from_end_of_file(filename, num_line):
    lines_list = read_list_of_lines(filename)
    for i in range(-num_line, 0, 1):
        print(lines_list[i])


#print_specific_number_line_from_end_of_file("read_data.txt", 3)


# tell() method : This method will tell you the current cursor position.
# seek method :  This method will help to set the cursor poition with respect to
# 1. Begining of file : seek(30, 0)
# 2. End of file : seek(-30, 2)
# 3. current position of cursor : (30, 1)

def set_different_cursor_position(filename):
    with open(filename, "rb") as file:
        print("start position of cursor :", file.tell())
        char_10 = file.read(10)
        print(char_10)
        print("current position of cursor :", file.tell())

        # set cursor at 30 position from begining of file
        # file.seek(30, 0)  # setting the cursor position from begining of file
        # file.seek(30, 1)  # set the cursor position from current position of the cursor
        file.seek(-30, 2) # set the cursor position from end of the file
        print("current position of cursor :", file.tell())
        print(file.read())


#set_different_cursor_position("read_data.txt")


# Write a python program to combine both the files with alternate lines and create new file.
def combine_two_files(file1, file2, file3):
    with open(file1, "r") as file1_obj:
        file1_list = file1_obj.readlines()

    with open(file2, "r") as file2_obj:
        file2_list = file2_obj.readlines()

    file3_list = []
    len_list = 0
    if len(file1_list) > len(file2_list):
        len_list = len(file1_list)
    else:
        len_list = len(file2_list)

    for i in range(len_list):
        file3_list.append(file1_list[i])
        file3_list.append(file2_list[i])

    with open(file3, "a") as file3_obj:
        for line in file3_list:
            file3_obj.write(line)



combine_two_files("read_file1.txt", "read_file2.txt", "append_file3.txt")
# Home work :
# 1. write a python program Replace file content JAVA with PYTHON.
# 2. write a python program to get all the email id from given file.
# 3. Write a python program to get all the phone number from given file.

#2. write a python program to get all the email id from given file.

def get_email_id(filename):
    email_list = []
    phone_numbers = []
    with open(filename, "r") as file:
        data = file.read()

    word_list = data.split()
    for word in word_list:
        if '@' in word:
            email_list.append(word)
        if len(word) == 10 and word.isnumeric():
            phone_numbers.append(word)

    print(email_list, phone_numbers)
    return email_list, phone_numbers

print("_"*50)
emails, phones = get_email_id("read_data.txt")

for email in emails:
    print(email)
print("_"*50)
for num in phones:
    print(num)


