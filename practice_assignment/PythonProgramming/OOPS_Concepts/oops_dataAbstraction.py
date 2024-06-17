"""
Abstraction : abstraction means to hide the details information from the user, just to provide overview of
              of the implimentation.
              abstraction can be achieved, when parent class method is implimented in the child class.


"""
class Animal:
    def animal_voice(self):
        pass

    def animal_name(self):
        pass

    def animal_category(self):
        pass

class Dog(Animal):

    def animal_voice(self):
        print("Dog Barks")

    def animal_name(self):
        print("Animal is Dog")


print(__name__)
if __name__ == "__main__":
    obj= Dog()
    obj.animal_voice()

