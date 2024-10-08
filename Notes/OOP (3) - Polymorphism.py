#----------------------------------------------------<Polymorphism>----------------------------------------------------

# ==> One method can do multiple functionalities and select its functionality according to the calling instance belongs to which class.

n1 = 5
n2 = 8
print(n1 + n2)


s1 = "Hello"
s2 = 'Python'
print(s1 + " " + s2)

#-----------------------------------------------------------------------------------------------------------------------

class A:
    def DoSomething(self):
        print("Class A")
        
class B(A):
    def DoSomething(self):
        print("Class B")

my = B()  
my.DoSomething() #The priority for Cuurrent Class
