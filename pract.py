dict1 = {"a":1,"b":2, "c": 3, "d":4}
dict2 = {}
for key,val in dict1.items():
    dict2[val]=key
print(dict2)
