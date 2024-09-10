"""
polymorphism : when one method perform the multiple tasks, then it is known as polymorphism

method overloading : When one class have two methods with same name and different parameters, then it
                     is known as method overloading. but python does not allow the method overloading
                     it only consider the latest defined method.
method overriding : when child class and parent class have same method name with same parameters then
                    child class method will override the parent class method, and it is known as method
                    overriding.
operator overloading :
"""

son_obj = None
class father:
    def __init__(self, fname='Mohal', fbusiness='ImportExport', fhouse="4 BHK"):
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

    def addition(self, num1, num2):
        print("addition of two numbers :", num1+num2)

    # This method will get priority
    def addition(self, num1, num2, num3):
        print("addition of three numbers :", num1+num2+num3)

    def multiplication(self, num1, num2):
        print("father class :multiplication of two number :", num1*num2)

    def math(self, num1: int, num2 : int) -> int:
        print("father class :multiplication of two number :", num1*num2)
        return num1*num2




class Son(father):

    def __init__(self, s_name='Rahul', s_education='BE', fname='Raghav', fbusiness='construction',
                 fhouse='Villa'):
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

    def multiplication(self, num1, num2):
        print("son class : multiplication of number :", num1*num2)

if __name__ == '__main__':
    obj = father()
    obj.addition(40, 50, 60)

    obj1 = Son()
    obj1.multiplication(5, 6)

# operator overloading : when one operator perform multiple task then it is known as operator overloading.

n1 = 60
n2 = 70
print("addition : ", n1+n2)
print("addition :", n1.__add__(n2))
print(dir(int))

s1 = 'Hello'
s2 = 'Good Morning'

print("add string :", s1+s2)
print("add string :", s1.__add__(s2))
print(dir(str))

print("multiplication :", n1*n2)
print("multiplication :", n1.__mul__(n2))

print(dir(list))
