func = lambda x, y:  x+y
print(func(50, 60))

def square(n):
    return n*n

# Map : Map function help to mapping of any function with list of inputs
list1 = [5, 7, 2, 8, 22, 3]
result = list(map(square, list1))
print(result)

result2 = list(map(lambda x:x*x, list1))
print("Result2 :", result2) # Result2 : [25, 49, 4, 64, 484, 9]
# Filter function : Filter the return the values on favorable condition

list2 =  [40, 13, 30, 44, 22, 17, 66, 2, 1, 33]
filter_result = list(filter(lambda x: x%2 ==0, list2))
print(" filter result :", filter_result) # [40, 30, 44, 22, 66, 2]

filter_result2 = list(filter(lambda x: x > 25, list2))
print(" filter result 2:", filter_result2) # [40, 30, 44, 66, 33]

# Reduce Function : Reduce function  provide a combine result

from functools import reduce
#       x    y
list3 = [55, 77, 33, 66, 23]
reduce_result = reduce(lambda x,y: x+y, list3)
print("reduce result :", reduce_result)


list4 = [1, 2, 3, 4]
reduce_result2 = reduce(lambda x,y: x*y, list4)
print("reduce result2 :", reduce_result2)
