

#1. Class Defination

class MyClass5:
    #1. Property
    age='',
    name=""
    #2. COnstructor
    def __init__(self,name,age):
        #The role of constructor is to initialize the class member
        self.name = name
        self.age = age

    #3. Method
    def displayMyName(self):
        print(f'My Name is { self.name } and my age is {self.age}')

o = MyClass5("ANIL DOLLOR",30)

# object.member
# object.method();
o.displayMyName()

