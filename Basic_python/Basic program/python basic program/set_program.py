set1 = {4, 7, "a", (1,2,3), True}
print(set1)
for val in set1:
    print(val)

# add method
set2 = {4, 7, 2, 8}
set2.add(50)
print(set2)


# update() method
set2.update(set1)
print(set2)

# union method
seta = {2, 4, 6}
setb = {'a', 'b', 'c'}
output = seta.union(setb)
print(output)


# remove/pop method
set5 = {'a', 'b', 'c', 'd' ,1, 5}
val = set5.pop()
print(val,set5)

val1 = set5.remove(5)
print(val1)

#  discard method
s1 = {4,7,22,45}
s1.discard(22)
print(s1)

# clear() method
set2 = {2,5,8,9,6}
set2.clear()
print(set2)

# difference update method
s3 = {2,4,5,7,9}
s4 = {1,3,4,6,8}
s3.difference_update(s4)
print(s4)

# difference method
set6 = {3, 6, 8, 9}
set5 = {1, 2, 6, 11}
res = set6.difference(set5)
print(res)


# intersection method
seta = {3, 6, 8, 9}
setb = {1, 2, 6, 11}
result = seta.intersection(setb)
print(result)

# intersection update
seta.intersection_update(setb)
print(seta)

# symmetric difference
set_a = {3, 6, 8, 9}
set_b = {1, 2, 6, 11}
r = set_a.symmetric_difference(set_b)
print(r)
# symmetric_difference update method
set_a.symmetric_difference_update(set_b)
print(Set_a)
print(set_b)

set_p = {5, 7, 22, 44, 12, 56}
set_q = {5, 7, 44}
set_r = {12, 7, 33}

print("set_q is subset:", set_q.issubset(set_p)) # True
print("set_r is subset:", set_r.issubset(set_p)) # False
print("set_p is superset :", set_p.issuperset(set_q)) # True

print("_"*50)
########################################
# copy method :

# shallow copy
set_h = {5, 7, 3, 8, 22, 33}
set_j = set_h
set_j.add(100)
print("set j:", set_j) #  {33, 3, 100, 5, 22, 7, 8}
print("set h:", set_h ) # {33, 3, 100, 5, 22, 7, 8}

# Deep copy
set_n = set_h.copy()
set_n.add(500)  # {33, 3, 100, 5, 22, 7, 8, 500}

print("set n :", set_n) # {33, 3, 100, 5, 22, 7, 8, 500}
print("set h:", set_h)

##################################################
# isdisjoint method: This method check if two sets are completely different to each other.
# if we have common value between two sets it will return False
# if we don't common value between two sets it will return True

print("_"*50)
set_a = {3, 6, 8, 11, 55}
set_b = {1, 2, 6, 9, 11, 3}
set_c = {33, 22, 44, 66}

result = set_a.isdisjoint(set_b)
print(" is disjoint :", result)  # False
result2 = set_a.isdisjoint(set_c)
print("setc is disjoint :", result2) # True





