def temp(func):
    def inner():
        print("_____ Welcome to Python_______")
        func()
        print("______Hope you Enjoy Learning _________")
    return inner

@temp
def greeting():
    print("Good Morning, Python is great language")

greeting()
