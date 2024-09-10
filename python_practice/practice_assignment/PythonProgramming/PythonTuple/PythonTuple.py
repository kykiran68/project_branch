tup1 = (4, 2.5, 'Hello', [4, 5, 7], {'a': 123, 'b' : 456}, 111, 234, (3, 6, 7))

print(tup1)

print(tup1[3])  # [4, 5, 7]

print(tup1[4]['b'])   # 456

# slicing in tuple
print(tup1[2:5])  # ('Hello', [4, 5, 7], {'a': 123, 'b': 456})
print(tup1[-3:])  # (111, 234, (3, 6, 7))
print(tup1[-1:-4:-1]) # ((3, 6, 7), 234, 111)
print(tup1[1::2]) # (2.5, [4, 5, 7], 111, (3, 6, 7))
print(tup1[::-1]) # ((3, 6, 7), 234, 111, {'a': 123, 'b': 456}, [4, 5, 7], 'Hello', 2.5, 4)


# apply loop on the tuple
tup3 = (4, 6, 98, 12, 34, 35)
for val in tup3:
    print(val)

print("_"*50)
for i in range(len(tup3)):
    print(i, tup3[i])

#

#### Tuple Methods #####

print(dir(tuple))
# 'count', 'index'

tup4 = (4, 6, 8, 22, 4, 7, 8, 22)
print(tup4.count(22)) # 2

print(tup4.index(8)) # 2

# delete tup variable
del tup4
# print(tup4)
# name 'tup4' is not defined.

# sorted function
tup5 = (3, 7, 2, 8, 12, 67, 1)

result = tuple(sorted(tup5))
print("result :", result)  # (1, 2, 3, 7, 8, 12, 67)

#### reversed function###
print("_"*50)
result = tuple(reversed(tup5))
print(result)
# print(next(result))
# print(next(result))
# print(tuple(result))
# print(result, [result])
# output = [data for data in result]
# print(output) # [1, 67, 12, 8, 2, 7, 3]
# for data in result:
#     print(data)

"""
# Get Max, Min and sum from tuple values
tup6 = (55, 66, 77, 33, 223, 266)
print("Max value:", max(tup6)) # Max value: 266
print("Mix value:", min(tup6)) # Mix value: 33
print("Sum of values:", sum(tup6)) # Sum of values: 720


########################
tup7 = (4, 7, 2, 66, 2)
print(tup7*3) # (4, 7, 2, 66, 2, 4, 7, 2, 66, 2, 4, 7, 2, 66, 2)

list1 = [5, 7, 8]
print(list1*3) # [5, 7, 8, 5, 7, 8, 5, 7, 8]

"""
values = (5, 8, 3, 9, 22, 12)
result = (x**2 for x in values)
print(result)
print(list(result)) # [25, 64, 9, 81, 484, 144]






