
def decorator(func):
    def inner():
        print("_"*50)
        func()
        print("_"*50)
    return inner


def function2(func):
    print("_"*50)
    func()
    print("_"*50)

@function2
def greeting():
    print("Welcome to Python Programming")


greeting()


def math_decorator(func):
    def inner(n):
        if n <= 20:
            func(n)
        else:
            func(20)
    return inner


@math_decorator
def square(n):
    for i in range(1, n):
        print(i**2, end=" ")

square(15)

