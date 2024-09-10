"""
class : class is nothing but the blueprint of the object, where we define all feature attributes/methods
        and variable related to the object
object : Object is entity through which we can access feature functionality of the class
         we can create n number of objects of any specific class.
constructor : constructor which initialize the memory of the class object.
            1. Default constructor : default it being called while creating the object.
            2. Parametrize constructor : constructor which has some parameter to pass while creating
            the object of the class.
variables : variable we declare to set the values in the class
            1. Instance variable : the variable which we declare with the help of self, then it
                                   instance variable.
            2. class variable : variable we declare on class level, then it is known as class variables.

methods :  When we declare any function inside the class then it is known as method.
             1. Instance method : Method we declare self as first parameter, then it is instance method.
             2. class method : Method we declare with @classmethod decorator and default
                              parameter will be cls, that can access only class variable, then it is known as class method.
             3. static method : Static methods are associated with class name not need to create
                               object of the class.
inheritance
polymorphism
data hiding
abstraction
"""


class ABC:
    """
    This class is for learning the OOPS concepts
    """

    Team = "CSK" # class variable
    city = "Mumbai"

    def __init__(self, num1, num2):
        print("objected initiated")
        self.x = num1  # instance variable
        self.y = num2  # instance variable

    # instance method
    def greeting(self):
        self.user_name = "Ashok"  # Instance variable
        print("Welcome to OOPS concept")

    def show_username(self):
        print("User name :", self.user_name)

    # instance method
    def addition(self):
        print("Addition :", self.x + self.y)

    def multiplication(self, n1, n2):
        print("multiplication :", n1*n2)

    def print_ipl_team_name(self):
        print("IPL Team name :", self.Team)

    @classmethod
    def show_class_variable(cls):
        print("class variable value :", cls.Team)
        city = "Bangalore"
        print("Print city name:", city)


    @staticmethod
    def show_factorials(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact *i

        print(f"Factorials of {num}:", fact)
    def get_factorials(self, num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact *i

        print(f"Factorials of {num}:", fact)

    def show_msg():
        print("Good Morning")


    def show_team_name(self):
        print("call by class name :", ABC.Team)
        print("call by class object (self) :", self.Team)

    def internal_calling(self):
        self.show_factorials(5)
        self.addition()
        self.multiplication(4, 5)
        self.show_class_variable()




obj = ABC(30, 40) # creating the object of the class
obj.greeting()
obj.addition()
obj.multiplication(5, 6)
print("Team name :", obj.Team)

obj.print_ipl_team_name()
obj.Team = "Mumbai"

obj.print_ipl_team_name()
###################################
print("_"*50)
obj2 = ABC(350, 400)
obj2.print_ipl_team_name()
obj2.Team = "RCB"
obj2.print_ipl_team_name()
obj2.show_class_variable()

######################################
print("_"*50)
ABC.show_factorials(6)
obj2.show_factorials(5)
ABC.print_ipl_team_name(obj2)

obj2.get_factorials(7)

obj2.z = 700

print("addition :", obj2.z + obj2.y)

####################################
print("_"*50)
obj2.greeting()
obj2.show_username()
obj2.show_team_name()

print(obj2.__module__)
print(obj2.__class__)
print(obj2.__doc__)

val = obj2.__getattribute__("x")
print("value of x", val)

val2 = obj2.__getattribute__("y")
print("value of y", val2)

obj2.__setattr__("x", 500)

valx = obj2.__getattribute__("x")
print("value of x", valx)

print("_"*50)
obj.internal_calling()
print("_"*50)
obj2.show_class_variable()

obj2.city = "Chennai"
print(obj2.city)
print(ABC.city)


