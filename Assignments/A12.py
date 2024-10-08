#----------------------------------------------------<1>----------------------------------------------------

def calculate(num1, num2, operation="add"):
    operation = operation.lower()
    
    if operation in ['a', 'add']:
        return num1 + num2
    elif operation in ['s', 'subtract']:
        return num1 - num2
    elif operation in ['m', 'multiply']:
        return num1 * num2
    else:
        return "Error: Invalid operation. Available operations are add, subtract, multiply."


print(calculate(10, 20))  
print(calculate(10, 20, "AdD"))  
print(calculate(10, 20, "a"))  
print(calculate(10, 20, "A"))  

print(calculate(10, 20, "S"))  
print(calculate(10, 20, "subTRACT"))  

print(calculate(10, 20, "Multiply"))  
print(calculate(10, 20, "m"))  

#----------------------------------------------------<2>----------------------------------------------------

def addition(*nums):
    total = 0
    for n in nums:
        if n ==10:
            continue
        elif n ==5:
            total -= n 
        else:
            total += n 
    return total           

print(addition(10, 20, 30, 10, 15))
print(addition(10, 20, 30, 10, 15, 5, 100))  

#----------------------------------------------------<3>----------------------------------------------------

def info(name, *skills):
    if skills == None:
        print(f"Hello {name}, You have no skills yet.")
    else:
        print(f"Hello {name}, Your Skills are:")
        for skill in skills:
            print('-',  skill)    
            
        
info('Salah', "HTML", "CSS", "JS", "Python")

#----------------------------------------------------<4>----------------------------------------------------

def say_hello(name = 'Unknown', age = 'Unknown', Country = 'Unknown'):
      print(f"Hello {name}, Your Country is {Country}")

say_hello('Salah', 21, 'Egypt')