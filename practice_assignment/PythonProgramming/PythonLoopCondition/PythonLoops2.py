num = 1
while num <= 10:
    print(num)
    num += 1

# run infinite while loop
print("_"*50)
while True:
    print(num)
    num += 1
    if num == 1000:
        break


"""
print("_"*50)
# write a python program for simple calculator
while True:
    print("Please select the math option to run\n"
          "1.  Addition\n"
          "2.  Multiplication \n"
          "3.  Division \n"
          "4.  Subtraction\n"
          "5.  Stop calculator")

    oprs_num = int(input("Please enter the operation number :"))
    if oprs_num <=4:
        num1 = int(input("Please enter the num1 value :"))
        num2 = int(input("Please enter the num2 value :"))

    if oprs_num == 1:
        print("Addition :", num1+num2)
    elif oprs_num == 2:
        print("Multiplication :", num1*num2)
    elif oprs_num == 3:
        print("Division :", num1//num2)
    elif oprs_num == 4:
        print("Subtraction :", num1-num2)
    elif oprs_num == 5:
        print("Thanks for using calculator !! closing ...")
        break

    print("_"*50)
"""

#### write a python program to reverse a number #####
print("_"*50)
"""
num1 = 123
revers_result = 0
temp = num1%10
print("temp =", temp)
revers_result = revers_result*10 + temp
print("reverse result :", revers_result)
num1 = num1//10
print("num1 = ", num1)

temp = num1%10
print("temp =", temp)
revers_result = revers_result*10 + temp
print("reverse result :", revers_result)

num1 = num1//10
print("num1 = ", num1)

temp = num1%10
print("temp =", temp)
revers_result = revers_result*10 + temp
print("reverse result :", revers_result)
"""

num1 = 7683456
rev_result = 0

while num1 > 0:
    temp = num1%10
    #print("temp =", temp)
    rev_result = rev_result*10 + temp
    #print("reverse result :", rev_result)
    num1 = num1//10

print("reverse result :", rev_result)









