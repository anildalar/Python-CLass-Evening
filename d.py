# import modulename

import c

# Create the object of the class

#object.member   --> Method

abc = c.MyClass3()

abc.tellMeYouSalary()


#1 Class Defination
class MyClass4:
    #1.Property
    age=30
    #2. Constructor only one especial function
    def __init__(self,name): # name is a formal argument
        print(' %s Your age is %s'%(name,self.age))
    #3. Method
    

#.2 Create CLass Object
qwerty = MyClass4('Anil') # 'Anil' actual Argment


