from abc import ABCMeta, abstractmethod

class Programming(metaclass = ABCMeta):
    
    def has_OOP(self):
        pass
    @abstractmethod
    def has_name(self):
        pass
class Python(Programming):
    def has_OOP(self):
        return 'Yes'
  
class Pascal(Programming):
    def has_OOP(self):
        return 'No'

one = Pascal()    
print(one.has_OOP())
