#----------------------------------------------------<Abstract>----------------------------------------------------

# - ABCs => Abstract Base Class --
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class

from abc import ABCMeta, abstractmethod

class Programming(metaclass = ABCMeta):
   
    @abstractmethod
    def has_OOP(self):
        pass
    
    def has_name(self):
        pass
    
    
    def high_level(self):
        pass
    
class Python(Programming):
    def has_OOP(self):
        return 'Yes'
  
class Pascal(Programming):
    def has_OOP(self):
        return 'No'

one = Pascal()    
print(one.high_level())