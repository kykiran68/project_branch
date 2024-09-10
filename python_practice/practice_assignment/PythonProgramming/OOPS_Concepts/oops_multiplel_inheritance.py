"""
Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A -> Class B, Class C -> Class B
Hierarchical Inheritance : Class A -> Class B , Class A -> Class C
"""
# Multiple Inheritance
class Mother:
    def __init__(self, m_name, m_business):
        self.m_name = m_name
        self.m_business = m_business

    def show_mother_details(self):
        print("Mother Name :", self.m_name)
        print("Mother Business:", self.m_business)

    def greeting(self):
        print("Hello my son how are you?")


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
class Son(father,Mother):

    def __init__(self, s_name, s_education, fname, fbusiness, fhouse, m_name, m_business):
        super().__init__(fname, fbusiness, fhouse)
        self.son_name = s_name
        self.son_education = s_education
        #self.m = Mother(m_name, m_business)
        self.m_name = m_name
        self.m_business = m_business

    def show_son_name(self):
        print("son name :", self.son_name)


    def show_son_education(self):
        print("son education :", self.son_education)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_education()
        self.greeting()

    def show_family_details(self):
        self.show_son_details()
        self.show_father_details()
        self.m.show_mother_details()



if __name__ == '__main__':
    obj = Son("Mohit", "Btech", "Raghavan", "Construction", "Bangalow", "Rohini", "Fashion")
    obj.show_family_details()


