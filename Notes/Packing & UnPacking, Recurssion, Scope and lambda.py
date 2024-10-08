# Packing, Unpacking
my_tuple = ("ML","Python",'JS','DL')
my_dict = {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  }

def show_skills(name, *skills, **skillsp):
  print(f"Hello {name}, Skills Without Progress:")
  for skill in skills:
      print(f"- {skill}")
      
  print("skills with Progress:")    
  for skill, value in skillsp.items():
        print(f"{skill} ==> {value}")
show_skills("Salah",*my_tuple, **my_dict)


#-----------------------------<Scope>-----------------------------


# Scope
x = 1         # Global Scope 

def one():
      global x     # Set the next variable global 
      x = 2       # Local Scope
  
      print(f"{x}")

def two():
      global x
      x = 4
      print(f"{x}")
one()  
two()
x = 3
print(x)

#-----------------------------<Recursion>-----------------------------
#Recursion --> I When you call FN inside itself to execute iterable instructions
# You must declare a base case (Stop Condition)
# When you reach base case the iterations stop and calculate instructions according to other instruction like; 
# if you have to calc n you must declare (Base Case) [ (n-1) / (n+1) ]
# You make swap between each function parameters
x = "WWWWoooooooorrrrlddd"


def clean_word(word):
      if len(word) ==1 :
            return word
      
      elif word[0] == word[1]      #"Woooooooorrrrlddd"
                                   #worrrrlddd
                                   #worlddd
                                   #wrldd
                                   #
            
            return clean_word(word[1:])  # It's remover for first charcter
                                         # Will remove first chracter   --> #"WWWoooooooorrrrlddd"
      else:
            
            return word[0] + clean_word(word[1:]) # This occurs when the condition not applies so, it will return first chracter and apply the clean confition to other words
print(clean_word(x))  

def tri_recursion(k):
    print(k)
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
def fun(x):
    # Print the current value of x
    print(x)
    
    # Base case: if x is 1, stop recursion
    if x == 1:
        return 1
    
    # Recursive case: return the sum of x and fun(x-1)
    return x + fun(x - 1)

# Calling the function and storing the result in 'val'
val = fun(5)

# Print the final result
print(val)




def clean_word(word):
  #base case
  if len(word) == 1:
    return word
  #remove repeated chracter (but for first one only) if exists
  elif word[0] == word[1]:
    return clean_word(word[1:])
  # reomve other repeated character
  else:
    return word[0] + clean_word(word[1:])
print(clean_word('WWWWoooooooorrrrlddd'))  

#-----------------------------<Lambda>-----------------------------
# Anonymous : No Name
# Need't defining
# Can return data from other functions
# Used for Simple Functions
# One Single Expression not block of code

def say_hello (name):
    return f"Hello {name}"
hello = lambda name : f"Hello {name}" 
print(hello('Salah'))
print(type(hello))

