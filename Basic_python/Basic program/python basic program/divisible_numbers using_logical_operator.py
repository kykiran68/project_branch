a = int(input("The entered number is: "))
if a%3 == 0 and a%7 == 0 and a%11 != 0:
    print("The number is divisible by 3,7 but not by 11")
elif a%3 == 0 and a%7 == 0 and a%11 == 0:
    print("The number is divisible")
else:
    print("The number is not divisible")