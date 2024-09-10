# Python program to get the Average of given numbers.
a = 50
b=30
c= 20
avg = (a+b+c)/3
print(avg)


n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",avg)