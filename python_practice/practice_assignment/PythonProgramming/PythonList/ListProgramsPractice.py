# write a python program to find the duplicate values from the list,
# and remove the duplicate value also.

list1 = [5, 7, 9, 22, 7, 5, 9, 11, 12]
duplicate = []
result = []

for val in list1:
    if val not in result:
        result.append(val)
    else:
        duplicate.append(val)

print("result :", result)
print("duplicate value :", duplicate)

# write a python move all positive value in right side and negative values in left side.
print("_"*40)
lista = [2, -4, -6, 7, 8, -22, 11, -16]
# positive = right side
# negative = left side
result = []

for val in lista:
    if val > 0:
        result.append(val)
    else:
        result.insert(0, val)

print("Result :", result)



