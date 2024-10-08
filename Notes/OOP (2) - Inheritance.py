#----------------------------------------------------<Inheritance>----------------------------------------------------

# Instructor is the first thing executing So take care for the functions in the instructor, It will Exeecute Fitsr.

#----------------------------------------------------<Example 1>----------------------------------------------------


class Food:    # Base Class
    
    def __init__(self, FName, Price):
        self.FName = FName
        self.Price = Price
        print(f"{self.FName} is Created From Main Class")
        
    def eat(self):
        
        print("Eat Method From Base Class")
        
        
class Apple(Food):    #Drived Class
    
    # To inherit Property from Parent class
    def __init__(self,FName, Price):
        
        super().__init__( FName, Price)
        print(f"{self.FName} is Created From Derived Class")
        
food_one = Food("Banana", 500)
food_two = Apple('Apple', 200)
food_one.eat()
food_two.eat()





#----------------------------------------------------<Example 2>----------------------------------------------------

class Family:
    def __init__(self,LName, number) :
        self.LName = LName
        self.number = number
        
    def Identification(self):
        print(f"You are Belonging to {self.LName} Family which contains {self.number} members.")


class Member(Family):
    def __init__(self, name, Job, LName, number):
        
        self.Job = Job
        super().__init__(LName, number)
        self.name = name

    def Welcome(self):
        print(f"Welcome Mr {self.name} You are {self.Job} \nYou are Belonging to {self.LName} Family which contains {self.number} members.")

member1 = Family('Abdelkhbair', 5)            
member1.Identification() 

member2 = Member('Salah', 'Ai Engineer', 'Badawy', 10)            
member2.Welcome()
member2.Identification() #Will Print Identifiaction method with Current (LName) value ==> Badawy



#----------------------------------------------------<Method Override>----------------------------------------------------

# ==> Method overriding occurs when a subclass defines a method with the same name as a method in its parent class.


#----------------------------------------------------<Multiple Inheritance , Method Resolution Orde (MRO)>----------------------------------------------------

class BaseOne:
    def __init__(self):
        print("Base One")

    def Fun1(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print("One")
        print(f"{self.n1 + self.n1}")    

class BaseTwo:
    def __init__(self):
        print("Base Two")
 
    
    def Fun2(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(f"{self.n1 * self.n1}")    

class Derived(BaseOne, BaseTwo):
    pass
        
n = BaseOne()
v = BaseTwo()
m = Derived()

m.Fun2(100,20)
m.Fun1(100,20)
print(Derived.mro())


