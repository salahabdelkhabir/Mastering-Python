#----------------------------------------------------<Modules>----------------------------------------------------

import random 
print(random)
print(random.random())

# Show all functions inside Modules
print(dir(random))

# Import one or two functions from moule
from random import randint 

#Import full modeule
import random 
from random import randint 

print(f"Print Random Integer {random.randint(100,900)}")

#----------------------------------------------------<Create Our Modules>----------------------------------------------------

import sys 
print(sys.path)
import sys 

def sayHello(name):
    print(f"Hello {name}")

def Welcome(name):
    print(f"Welcome {name}")
    
sys.path.append(r"D:\Mastering Python")
print(sys.path)
import Modules
print(dir(Modules))
Modules.sayHello('Salah')