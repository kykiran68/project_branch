import time

import psutil as psutil


def greeting():
    return "good morning"
    return "Good Evening"


def messages():
    yield "Good Morning"
    yield "How are you"
    yield "Hope you are doing good"
    yield "Welcome to python Programming"


obj = messages()
print(obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
#print(next(obj))

for val in obj:
    print(val)


# list1 = [5, 7, 8, 2, 6, 22, 33]
# output = reversed(list1)
# print(output)

def print_list_values():
    list1 = [4, 6, 7, 1, 8, 2]*100000
    t1 = time.time()
    for val in list1:
        print(val, end='')
    t2 = time.time()
    print("total time taken :", t2-t1)
    print("CPU usage :", psutil.cpu_percent(8))
    print("CPU usage :", psutil.virtual_memory())

print_list_values()

def print_list_values_gen():
    list1 = [4, 6, 7, 1, 8, 2]*100000
    for val in list1:
        yield val

obj = print_list_values_gen()

ta = time.time()
for data in obj:
    print(data, end='')
tb = time.time()

print("CPU Usage :", psutil.cpu_percent(8))
print("CPU usage :", psutil.virtual_memory())
print("total time take:", tb-ta)
