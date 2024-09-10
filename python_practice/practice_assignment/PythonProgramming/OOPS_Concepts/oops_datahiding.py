"""
Datahiding : In python data hiding is achived by defining the variable and methods with single under score
            and double undescore as prefix.
            1. If we defined any variable/method name with single underscore as prefix then those class
               will not available in suggestion list, but we can directly access with the class object.

            2. If we defined any variable/method name with double underscore as prefix then those class members
               will not available in suggestion list, but we can directly access with the class name.
               e.g _<classname>__<method/variable>


"""

class Car:
    def __init__(self, car_name, car_comp, car_price):
        self.car_name = car_name
        self._car_company = car_comp
        self.__car_price = car_price

    def show_car_name(self):
        print("Car name :", self.car_name)

    def _show_car_company(self):
        print("Car company :", self._car_company)

    def __show_car_price(self):

        print("Car price :", self.__car_price)

if __name__ == "__main__":
    obj = Car('Harier', 'TATA', '25L')

    obj._show_car_company()
    obj._Car__show_car_price()
    print(dir(obj))

