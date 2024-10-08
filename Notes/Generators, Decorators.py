#----------------------------------------------------<Generators>----------------------------------------------------


# It depending on Yield Instead of return.
# Returns Generator Iterator via Calling Yield. 
# It supports next() so it gives iteration.
# Not Starting Automatically, It Give you Control.
# The crucial Point --> It resume From where it called not From begining like in loop.  

def my_grnerator():
    yield 5
    yield 9
    yield 1
    yield 3
    yield 7

MyGen = my_grnerator()    

print(next(MyGen))
print(next(MyGen))
print(next(MyGen))

print('Loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooook')


# Look you can't make iteration twice because you have reached last iterated element 
# So you can iterate via nex() method or for loop or patitiong the iterated data like bellow:

for number in MyGen:
    print(number)

#----------------------------------------------------<Decorators>----------------------------------------------------

# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# [6] You can use muliple decorators on one function.

# ----------------------------------------------------------------------

def MyDocerator(FN): #Decorator

    def NestedFN(a1, b1):        
        print("Before")  # Message From Decorator 
        FN(a1, b1)             # The Decorated function
        print("After")   # Message From Decorator   
        return NestedFN
    
# def sayHello():
#     print("Hello!")            
    
# afterDecoration = MyDocerator(sayHello)    

# Sugar Syntax --> Apply decoration before one decorated FN.

@MyDocerator
def sayHello():
     print("Hello!")   
     
@MyDocerator     
def sayWelcome():
    print("Welcome")     
    
@MyDocerator 
def calculate(a, b):
    print(a + b)
calculate(10, 90)

#------------------------------------------------------------------------------------------------------------

def MyDocerator(FN): #Decorator

    def NestedFN(*numbers):        
        for number in numbers:
            if number <0:
                print("Beware One of these numbers is less than 0")
        FN(*numbers)             # The Decorated function
        
    return NestedFN
    
@MyDocerator 
def calculate(a, b, c):
    print(a + b)
calculate(10, -90, 0)
#------------------------------------------------------------------------------------------------------------
from time import time
def speedTest(fn):
    def wrapper():
        start = time()
        fn()
        end = time()
        print(f"Function Running Time Is: {end - start} ")
    return wrapper


@speedTest
def bigloop():
    for number in range(1,20000):
        print(number)
        
bigloop()        