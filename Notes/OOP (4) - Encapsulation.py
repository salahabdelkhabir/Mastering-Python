#----------------------------------------------------<Encapsualtion>----------------------------------------------------

# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# We have 3 phases ==> [Public, Protected and Private]


#----------------------------------------------------<Public>----------------------------------------------------

# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class

class Member:
    def __init__(self, name):
        self.name = name
        
one = Member('Salah')
print(one.name)        
one = Member('Ahmed')
print(one.name)        


#----------------------------------------------------<Protected>----------------------------------------------------

# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _

class Member:
    def __init__(self, name):
        self._name = name
        
one = Member('Salah')
print(one._name)        
one = Member('Ahmed')
print(one._namename)        
#----------------------------------------------------<Private>----------------------------------------------------

# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores  __

class Member:
    def __init__(self, name):
        self.__name = name             # Private attribute
    def say_hello(self) :              # You Can Access Attribute Via Method
        return f"Hello, {self.__name}"   


# ====> Note that: Python doesn't provide real restriction via _ or __ 
# Look at last last line
one = Member('Salah')
print(one.say_hello())            
print(one._Member__name)

#----------------------------------------------------<Getters, Setters>----------------------------------------------------
class Member:
    
    def __init__(self, name):
        self.__name = name             

    def say_hello(self) :              
        return f"Hello, {self.__name}"   

    def get_name(self):  #Getter
        return self.__name    
    
    def set_name(self, newName):  #Setter
        self.__name = newName

one = Member('Salah')
print(one.get_name())
one.set_name('Ahmed')
print(one.get_name())


#----------------------------------------------------<Property Decorator>----------------------------------------------------

# We can Convert Method to attribute via Property Decorator ' @property '
class Member:
    
  def __init__(self, name, age):

    self.name = name

    self.age = age
   
  def say_hello(self):

    return f"Hello {self.name}"
  @property
  def age_in_days(self):

    return self.age * 365

one = Member("Salah", 21)

print(one.name)
print(one.age)
print(one.say_hello())
print(one.age_in_days)