"""
Design and implement a python program for managing student information using object-oriented principles. create a class called 'Student' with encapsulated attributed for name,age, and roll number. implement getter and setter for these attributrs. additionaly, provide methods to display student information and update student detail
TASKS:
Define the 'Student' class with encapsulated attributes.
implement getter and setter method for the attributes.
write methods to display student information and update details.
create instance of the'Student' class and test the implemented functionally.
"""
class Student:
    def __init__(self,name,age,roll_no):
        self.__name = name
        self.__age = age
        self.__roll_no = roll_no
    
    def set_update_detail(self,name,age,roll_no):
        self.__name = name
        self.__age = age
        self.__roll_no = roll_no

    def get_display_detail(self):
        print("Name :",self.__name)
        print("Age :",self.__age)
        print("Roll no. :",self.__roll_no)

student = Student()
student.set_update_detail("Anjani",19,240010150018)
student.get_disply_detail()