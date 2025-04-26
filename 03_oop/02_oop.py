# delete
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Anjani")
print(s1.name)
del s1.name # delete object property
del s1    # delete object
print(s1)

# public and private
# public that can used outside class
# private that cannot used outside class

class Account:
    def __init__(self,account_no,account_password):
        self.account_no = account_no # public attribute
        self.__account_password = account_password # private attribute __ before attribute

    def reset_password(self):
        print(self.__account_password) # here we can pass ,it is inside class

customer = Account(1000001,"abcde")
print(customer.account_no) # it is public
customer.reset_password()
print(customer.__account_password) # not print , it is private

## Inheritance
class Car:
    @staticmethod
    def start():
        print("car start.....")

    @staticmethod
    def stop():
        print("car stop....")

    def car_owner(self,name):
        self.owner = name
        print("%s is the owner of this car"%self.owner)

class Car_type(Car):
    def __init__(self,source):
        self.source = source
        print("stay tuned....")


class Car_floor_color:
    def __init__(self,floor_color):
        self.floor_color = floor_color

class Car_color(Car,Car_floor_color):
    def __init__(self,color,floor_color):
        super().__init__(floor_color)
        self.color = color
        super().start()

class Fortuner(Car_type):
    def __init__(self,model):
        self.model = model

# print(car1.start())
# print(car1.stop())

car2 = Car_color("White","Black")
print("car color :",car2.color)
print("car floor color :",car2.floor_color)

car3 = Car()
car3.car_owner("Anjani")

class Person:
    name = "unknown"
    def change_name(self,name):
        self.name = name # it change name of only object attribute not class attribute

p1 = Person()
p1.change_name("Anjani")
print(p1.name)
print(Person.name)


# @classmethod
class Person:
    name = "unknown"
    def change_name(self,name):
        Person.name = name # it change name of both class and object attribute

p1 = Person()
p1.change_name("Anjani")
print(p1.name)
print(Person.name)

class Person:
    name = "unknown"
    def change_name(self,name):
        self.__class__.name = "Anjani" # it change name of both class and object attribute
        

p1 = Person()
p1.change_name("Anjani")
print(p1.name)
print(Person.name)

class Person:
    name = "unknown"

    @classmethod   
    def change_name(obj,name):
        obj.name = name
        

p1 = Person()
p1.change_name("Anjani")
print(p1.name)
print(Person.name)

# @proprtymethod
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def calculate_percentage(self):
        percentage = str((self.phy+self.chem+self.math)/3) + "%"
        print(percentage)

student1 = Student(98,94,99)
student1.phy = 20
print(student1.calculate_percentage)