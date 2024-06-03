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
            2. class variable :

methods :  When we declare any function inside the class then it is known as method.
             1. Instance method
             2. class method
             3. static method
inheritance
polymorphism
data hiding
abstraction
"""

class ABC:
    team = 'CSK'
    def __init__(self,num1,num2):
        print("This is parameterized constructor")
        self.x = num1
        self.y = num2
    def greeting(self):
        print("Welcome!!!!!!!! We are learning OOP concept")
    def addition(self):
        print("Addition: ",self.x + self.y)
    def multiplication(self,n1,n2):
        print("Multiplication is : ",n1*n2)
    def ipl_team_name(self):
        print("IPL team name is : ",self.team)
    @classmethod
    def show_class_variable(cls):
        print("Class variable value : ",cls.team)

    @staticmethod
    def show_factorials(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact * i

        print(f"Factorials of {num}:", fact)

    def get_factorials(self, num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact * i

        print(f"Factorials of {num}:", fact)

    def show_msg():
        print("Good Morning")

    def show_team_name(self):
        print("call by class name :", ABC.team)
        print("call by class object (self) :", self.team)

    def internal_calling(self):
        self.show_factorials(5)
        self.addition()
        self.multiplication(4, 5)
        self.show_class_variable()


obj = ABC(30, 40)
obj.addition()
obj.greeting()
obj.multiplication(2,3)
print("Team name : ", obj.team)
obj2 = ABC(350, 400)
obj2.ipl_team_name()
obj2.Team = "RCB"
obj2.ipl_team_name()
obj2.show_class_variable()

obj.ipl_team_name()
obj.team = "Mumbai"
obj.ipl_team_name()
obj2.greeting()
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

class father:
    def __init__(self, fname, fbusiness, fhouse="4 BHK"):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print("Father Name :", self.fname)

    def show_father_business(self):
        print("Father Business :", self.fbusiness)

    def show_father_father_house(self):
        print("Father house :", self.fhouse)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_father_house()
class Son(father):

    def __init__(self, s_name, s_education, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.son_name = s_name
        self.son_education = s_education

    def show_son_name(self):
        print("son name :", self.son_name)

    def show_son_education(self):
        print("son education :", self.son_education)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_education()
    def show_family_details(self):
        self.show_father_details()
        self.show_son_details()

# obj = Son("Mohit", "Btech", "Raghavan", "Construction", "Bangalow")
# obj.show_family_details()
# print(obj.__module__)
# print(__name__)

# if __name__ == '__main__':
#     obj = Son("Mohit", "Btech", "Raghavan", "Construction", "Bangalow")
#     obj.show_family_details()
#     print(obj.__module__)
#     print(__name__)

obj_1 = Son("Mohit", "Btech", "Raghavan", "Construction", "Bangalow")
class Mother:
    def __init__(self, m_name, m_business):
        self.m_name = m_name
        self.m_business = m_business

    def show_mother_details(self):
        print("Mother Name :", self.m_name)
        print("Mother Business:", self.m_business)


class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print("Father Name :", self.fname)

    def show_father_business(self):
        print("Father Business :", self.fbusiness)

    def show_father_father_house(self):
        print("Father house :", self.fhouse)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_father_house()


# MRO : Method Resolution Order
class Son(father, Mother):

    def __init__(self, s_name, s_education, fname, fbusiness, fhouse, m_name, m_business):
        super().__init__(fname, fbusiness, fhouse)
        self.son_name = s_name
        self.son_education = s_education
        self.m = Mother(m_name, m_business)

    def show_son_name(self):
        print("son name :", self.son_name)

    def show_son_education(self):
        print("son education :", self.son_education)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_education()

    def show_family_details(self):
        self.show_son_details()
        self.show_father_details()
        self.m.show_mother_details()



if __name__ == '__main__':
    obj = Son("Mohit", "Btech", "Raghavan", "Construction", "Bangalow", "Rohini", "Fashion")
    obj.show_family_details()

class GrandFather:
    def __init__(self, GF_name, GF_property):
        self.GF_name = GF_name
        self.GF_property = GF_property

    def show_grand_father_details(self):
        print("Grand Father Name :", self.GF_name)
        print("Grand Father Property :", self.GF_property)


class father(GrandFather):
    def __init__(self, fname, fbusiness, fhouse, GF_name, GF_property):
        super().__init__(GF_name, GF_property)
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print("Father Name :", self.fname)

    def show_father_business(self):
        print("Father Business :", self.fbusiness)

    def show_father_father_house(self):
        print("Father house :", self.fhouse)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_father_house()

class Son(father):

    def __init__(self, s_name, s_education, fname, fbusiness, fhouse, GF_name, GF_property):
        super().__init__(fname, fbusiness, fhouse, GF_name, GF_property)
        self.son_name = s_name
        self.son_education = s_education

    def show_son_name(self):
        print("son name :", self.son_name)

    def show_son_education(self):
        print("son education :", self.son_education)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_education()

    def show_family_details(self):
        self.show_father_details()
        print("_"*50)
        self.show_son_details()
        print("_"*50)
        self.show_grand_father_details()


if __name__ == '__main__':
    obj = Son("Mohit", "Btech", "Raghavan", "Construction", "Bangalow", "MohanLal", "100 ACR")
    obj.show_family_details()
    print(obj.__module__)
    print(__name__)
    obj.show_family_details()
class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print("Father Name :", self.fname)

    def show_father_business(self):
        print("Father Business :", self.fbusiness)

    def show_father_father_house(self):
        print("Father house :", self.fhouse)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_father_house()

class Son1(father):

    def __init__(self, s_name, s_education, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.son_name = s_name
        self.son_education = s_education

    def show_son_name(self):
        print("son name :", self.son_name)

    def show_son_education(self):
        print("son education :", self.son_education)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_education()

    def show_family_details(self):
        self.show_father_details()
        print("_"*50)
        self.show_son_details()
        print("_"*50)

class Son2(father):

    def __init__(self, s_name, s_education, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.son_name = s_name
        self.son_education = s_education

    def show_son_name(self):
        print("son name :", self.son_name)

    def show_son_education(self):
        print("son education :", self.son_education)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_education()

    def show_family_details(self):
        self.show_father_details()
        print("_"*50)
        self.show_son_details()
        print("_"*50)



if __name__ == '__main__':
    obj1 = Son1("Mohit", "Btech", "Raghavan", "Construction", "Bangalow")
    obj1.show_family_details()
    print("_"*40)
    obj2 = Son2("Roshan", "BA", "Raghavan", "Construction", "Bangalow")
    obj2.show_family_details()

