#----------------------------------------------------<1>----------------------------------------------------

def reverse_string(my_string):
      for c in reversed(my_string):
          yield c

for c in reverse_string("Elzero"):
  print(c)
  
#----------------------------------------------------<2>----------------------------------------------------

def My_Decorator(FN):
    
    def NestedFN():
        print('Sugar Added From Decorators')
        FN()
        print('#' *50)
    return NestedFN    
@My_Decorator

def make_tea():
      print("Tea Created")
      
@My_Decorator

def make_coffe():
  print("Coffe Created")
  
make_tea()
make_coffe()