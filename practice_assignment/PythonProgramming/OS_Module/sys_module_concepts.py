import sys

print(sys.version_info) # sys.version_info(major=3, minor=12, micro=2, releaselevel='final', serial=0)
print(sys.version) # 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)

print(sys.platform) # win32
#
# user_inputs = sys.argv
# print(user_inputs)
#
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# print("addition :", num1+num2)


################### sys.exit() to stop file execution ##############

print("_"*50)
for i in range(30):
    print(i)
    if i == 20:
        exit()
        #break


print("Execution completed")
