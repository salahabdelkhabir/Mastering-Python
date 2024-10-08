#----------------------------------------------------<1>----------------------------------------------------
num = int(input("Add Your Number"))

if num > 9:
    raise IndexError("Only One Character Allowed")
 
elif num == 0:
      raise ValueError(" Number Must Be Larger Than 0")  

elif type(num) is str:
    raise Exception("Only Numbers Allowed")

else:
    print(f"The Number Is {num}")
    
#----------------------------------------------------<2>----------------------------------------------------

LETTER = input("Add Letter From A to Z: ")

try:
    if len(LETTER) != 1:
        raise IndexError("You Must Write One Character Only")
    if not LETTER.isalpha() or not LETTER.isupper():
        raise ValueError("The Letter Not In A - Z")
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print(f"You Typed {LETTER}")

#----------------------------------------------------<3>----------------------------------------------------

def calculate(num1: int, num2: int) -> int:
    return num1 + num2

print(calculate(20, 30))