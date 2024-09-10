marks = int(input("Enter the marks: "))
if 0 < marks < 40:
    print("you are fail in examination with marks", marks)
elif 40<= marks <= 60:
    print("you are passed with third division. your marks is ", marks)
elif 60 < marks <= 80:
    print("you are passed with second division. your marks is ", marks)
elif 80 < marks <= 100:
    print("congratulations! you are passed with first division. your marks is ", marks)
else:
    print("invalid marks")