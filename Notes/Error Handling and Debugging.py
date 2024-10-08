#----------------------------------------------------<Raise Exceptions>----------------------------------------------------

# Errors and Exceptions Raising
# There are many types but you have to know what is the error and it's type and how to raise your exception


x = 10

if x > 0:
    raise Exception(" The number is less than 0")
    print("This will not be printed")
else:
    print("Well number") 
print("After conditionala excecution")       

#----------------------------------------------------<Try, Else, Finally>----------------------------------------------------
# Try ==> Test Your Code
try:
    
    number =int(input("Write Your Age : "))
    
except:      # Handle the Errors if Founded
    
    print("This is not Integer")
    
else:        # If there is no errors
    print("Thank you")
    
finally:     # Print whatever
    print("Print Finally")
    
#----------------------------------------------------<Advanced Example>----------------------------------------------------

try:
    print(10/0)

except ZeroDivisionError:
    print("Can't Divide number on Zero")
except NameError:
    print("Identifier Not Found")
except ValueError:
    print("Value Error")
except: # (If any other unselected errors)
    print("Error Happens")    
    
#----------------------------------------------------<Advanced Example>----------------------------------------------------

the_file = None
the_tries = 5

while the_tries > 0:
    
    try:
        
        print("Enter The File Name Without Absolute Path")
        print(f"{the_tries} Tries Left")
        print(r"D:\Mastering Python\Notes")
        file_name = input('Enter Your File Name').strip()
        the_file = open(file_name, 'r')
        print(the_file.read())
        break
    
    except:
        
        print("Be Sure The Name Is Valid")
        the_tries -= 1
        
else : 
    
    print("All tries Are Done")
    
#----------------------------------------------------<Debugging>----------------------------------------------------

my_list = [1, 2, 3, 4, 5, 6]

my_dictionary = {"Name": "Osama", "Age": 36, "Country": "Egypt"}

for num in my_list:

  print(num)

for key, value in my_dictionary.items():

  print(f"{key} => {value}")

def function_one_one():

  print("Hello From Function One")

function_one_one()

#----------------------------------------------------<Type Hinting>----------------------------------------------------

#--> Used for Developers to hint the function 
def say_Hello(name: str) -> str:
    print(f" Hello, {name}")
say_Hello(10)    