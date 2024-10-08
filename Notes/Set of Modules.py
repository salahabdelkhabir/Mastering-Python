#----------------------------------------------------<ZIP>----------------------------------------------------

# Loop on Many Iterators with zip()
# Zip() --> Returns object contains all objects
# Zip length is the length of lowest object.

list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C']
tuple1 = ('Man', 'Woman', 'Girl', 'Boy')
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}
ultimatelist = zip(list1, list2, tuple1, dict1)
print(ultimatelist)

for item1, item2, item3, item4 in ultimatelist:
    print('List 1 Item  ==>', item1)
    print('List 2 Item  ==>', item2)
    print('Tuple 1 Item  ==>', item3)
    print('Dictionary 1 Key  ==>',item4, 'and', 'Dictionary 1 Value ==>',  dict1[item4])
    

#----------------------------------------------------<PILLOW>----------------------------------------------------

from PIL import Image
myImage = Image.open(r'D:\Mastering Python\Notes\image.png')
myImage.show()

# My Cropped Image
myBox = (0, 0, 400, 400)
myNewImage = myImage.crop(myBox)
myNewImage.show()

# Converted image
MyConverted = myImage.convert('L')
MyConverted.show()

#----------------------------------------------------<Commenting Vs Documenting String>----------------------------------------------------

# Documenting String ==> Meant for documenting modules, classes, and functions and can be accessed programmatically.
# Commenting ==> Meant to clarify the code for developers but cannot be accessed programmatically.

def salah(name):
    # """ This is Function to Say Hello From Salah """

    """
        I say Hello everyone here.    
    """

    print(f"Hello, {name}")

salah("Salah")
print(salah.__doc__)

#----------------------------------------------------<PYLint>----------------------------------------------------

#--> To see Pylint Analysis : Pylint.exe "d:\Mastering Python\Notes\tempCodeRunnerFile.py"
def say_hello(name):
    return (f"Hello {name}")

print(say_hello('Ahmed'))