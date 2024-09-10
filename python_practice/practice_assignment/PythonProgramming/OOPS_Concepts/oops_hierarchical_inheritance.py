"""
Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A -> Class B, Class C -> Class B
Hierarchical Inheritance : Class A -> Class B , Class A -> Class C
"""
# Hierarchical Inheritance
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



