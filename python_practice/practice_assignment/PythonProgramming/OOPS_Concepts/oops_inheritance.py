"""
Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A -> Class B, Class C -> Class B
Hierarchical Inheritance : Class A -> Class B , Class A -> Class C
"""
son_obj = None
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
