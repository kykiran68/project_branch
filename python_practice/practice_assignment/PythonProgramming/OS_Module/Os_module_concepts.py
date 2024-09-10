import os
import shutil
import random

# get current working directory path

cur_path = os.getcwd()
print("cur path :", cur_path)
# E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Deepesh\OS_Module

# Change working directory path


#os.chdir(r"E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Ashok")
#print(os.getcwd())
# E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Ashok


#Get list of all files and folder from target location
tar_path = r"E:\Filesdata"
file_folder_list = os.listdir(tar_path) # This will provide list of all files and folder
print(file_folder_list)

# join path with os.path.join()
for data in file_folder_list:
    print(data)
    data_path = os.path.join(tar_path, data) # This will join two paths
    print(data_path)

    # os.path.isfile # This will check given path is file
    # os.path.isdir # this will check the given path is directory or not
    if os.path.isdir(data_path):
        print("Folder")
    elif os.path.isfile(data_path):
        print("File")

    print("_"*40)



################ CHeck if the path is file or not ################

print(os.path.isfile(r"E:\Filesdata\count_name.txt")) #True

# check given location exist or not
result1 = os.path.exists(r"E:\Filesdata\count_name.txt") # True
print("File exist or not :", result1)
result2 = os.path.exists(r"E:\Filesdata\count_name123.txt") # False
print("File exist or not :", result2)

##################################################################
# create directory or current location
# os.mkdir("folder1")

# create directory on target location:
# os.mkdir(r"E:\Filesdata\GTM_BATCH4")

# create multi level folder directory
# os.makedirs(r"E:\Filesdata\GTM_BATCH4\f1\f2\f3")

# Remove empty directory
# os.rmdir(r"E:\Filesdata\GTM_BATCH3")

# Remove non empty directory
# os.removedirs(r"E:\Filesdata\GTM_BATCH4")

# Remove non empty directory
# shutil.rmtree(r"E:\Filesdata\GTM_BATCH4")

# copy files from one location to another location
src_location = r"E:\Filesdata\file1.txt"
tar_location = r"E:\Filesdata\Tavet\file1_batch2_copy.txt"
shutil.copy(src_location, tar_location)

############# Get value from environment variable ###################

val = os.getenv("Browser2")
print("value :", val)

path = os.getenv("path")
print("path value :", path)

chrome_path = os.getenv("CHROME_PATH")
print("chrmepath :", chrome_path)

############ Get size of file ###############

filesize = os.path.getsize(r"E:\Filesdata\Tavet\file_copies.txt")
print("File size :", filesize)
# File size : 118549760

########## Get CPU count ##############

cpu_count = os.cpu_count()
print("cpu count of system :", cpu_count)
# cpu count of system : 8

################# get mtime of the file ############

mtime = os.path.getmtime(r"E:\Filesdata\Tavet\file_copies.txt")
print("mtime :", mtime)# 1713753877.4982724

########### Run windows command ##########
# os.system("control") # open control panel of windows

# os.system("appwiz.cpl") # open program feature

# os.system("dir E:\Filesdata")  # get all file folder data

# execute the python file using os module.
# os.system("python E:\\Trainings\\GTM_PS_Batch03_8March2024\\GTM_PS_Batch03\\Deepesh\\ReadWriteExcelFile\\read_json_file.py")

######### Check file permission ############
permission = os.access(r"E:\Filesdata\Tavet\file_copies.txt", os.X_OK)
print("File permission :", permission)
"""
mode	Required.
os.F_OK: Checks if the path exists.
os.R_OK: Checks if the path is readable.
os.W_OK: Checks if the path is writable.
os.X_OK: Checks if the path is executable.
"""

#################### Generate random string in python ############

output = os.urandom(100)
print("random string :", output)  #$ \xd4\x9a\x86[\xac\x8bG-


#################### Generate random integer ##############
print("_"*40)
# return any random in given values
result = random.randint(1000, 2000)   # 1902
print(result)

# return any random value in given range along with difference value as like range method.
val = random.randrange(2, 10, 2)
print("val  :", val, type(val))

# it will provide random floating number 0 to 1
val2 = random.random()
print(val2) #0.35347856816623346


print("_"*40)

# generate random binary numbers
bin = ''

for i in range(10):
    val = random.randint(0, 1)
    bin = bin + str(val)

print(bin)


###############################
print("_"*50)
number = random.getrandbits(10)
print(number, format(number, "0b"))

