#----------------------------------------------------<1>----------------------------------------------------

import sys
import random
import inspect

random_number = random.randint(10, 50)
print(f"Random Number Between 10 And 50 => {random_number}")

random_even_number = random.choice([x for x in range(2, 11) if x % 2 == 0])
print(f"Random Even Number Between 2 And 10 => {random_even_number}")

random_odd_number = random.choice([x for x in range(1, 10) if x % 2 != 0])
print(f"Random Odd Number Between 1 And 9 => {random_odd_number}")

print("Module Methods:")

for name, obj in inspect.getmembers(random):
    if inspect.isfunction(obj):
        print(name)

#----------------------------------------------------<2>----------------------------------------------------

def say_hello():
    return "Hello Osama"

def say_welcome():
    return "Welcome Osama"
sys.path.append(r"D:\Mastering Python")
print(sys.path)
import A17
print(A17.say_hello())
print(A17.say_welcome())

#----------------------------------------------------<3>----------------------------------------------------

from A17 import sw

print(sw())

#----------------------------------------------------<4>----------------------------------------------------

from A17 import new_welcome as nw

print(nw())