# create class
class Student:
    name = "Anjani"
    roll_no = 240010150018

# create object
student_object = Student()
print(student_object)
print(student_object.name,student_object.roll_no)
print(type(student_object))

###

# create class
class Student:
    college_name = "ABC college" # class attribute
    # default constructor
    def __init__(self):
        pass

    # Parameterized constructor

    def __init__(self,full_name,marks):
        print("New student added in Database.....")
        print("Hello,",full_name)
        # print(self) # self is s1 or s2
        self.name = full_name  # object attribute
        self.marks = marks    # object attribute
        print(self.name,self.marks,self.college_name)
        

# create object
s1 = Student("Anjnai",97)
s2 = Student("Ravi",98)

############

class Student:
    def __init__(self,full_name,marks):
        self.name = full_name
        self.marks = marks

    def welcome(self):
        print("Hey welcome",self.name)

    def mark(self):
        print(self.marks)

s1 = Student("Anjani",97)
s1.welcome()
s1.mark()

## EXERCISE
# create student class that take name & marks of 3 subjects as arguments in constructor. thrn create a method to print the average

class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def welcome(self):
        print("Hey welcome",self.name)
    
    def avg_marks(self):
        average_marks = (self.marks1+self.marks2+self.marks3)/3
        print(round(average_marks,2))

student_detail = Student("Anjani",97,95,98)
student_detail.welcome()
student_detail.avg_marks()
print("Program executed sucessfully.........")

# we can also change name 
student_detail.name = "Ravi"
student_detail.welcome()

## static methods
# method that don't use self parameter work at class level 
# @staticmethod   it is called decorator

class Student:
    def __init__(self,name):
        self.name = name

    def welcome(self):
        print("Hello",self.name)

    @staticmethod
    def wish():
        print("Thank you")

s1 = Student("Anjani")
s1.welcome()
s1.wish()

####  EXERCISE
# create account class with 2 attribute balance & account number, create a method for debit, credit & print available balance
class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        self.balance -= amount
        print("Debit amount :",amount)
        print("Available amount :",self.balance)
    
    def credit(self,amount):
        self.balance += amount
        print("Credit amount :",amount)
        print("Available amount :",self.balance)

    @staticmethod
    def wish():
        print("Thank you for banking with us")

cus = Account(20000,100001)
cus.debit(1000)
cus.credit(40340)
cus.credit(1000)
cus.credit(20940)
cus.debit(20786878768)
cus.wish()