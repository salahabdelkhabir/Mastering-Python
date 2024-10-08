#------------------------------<While>----------------------

# The boundary can be in any place but take care about its position action
a = 2
while a<10:
    a += 1 
    print(a)
else:
    print('Loop ended')    

MyF = ['Youssef', 'Salah', 'Ashraf', 'Tarek', 'Abdelrahman' ]

a = 0
while a < len(MyF):
    print(MyF[a])
    a += 1
print(MyF[0])
print(MyF[1])
print(MyF[2])
print(MyF[3])
print(MyF[4])
print(MyF[5])
print(MyF[6])
print(MyF[7])
print(MyF[8])
print(MyF[9])
 
 
 
myFavWeb = []
maxwebs = 5
while maxwebs > 0:
    
    # Input The New Website
    web = input("Website Name wthout https://")
    myFavWeb.append(f"https://{web.strip().lower()}")
    # Decrease one from allowed websites
    maxwebs -= 1
    #print add message
    print(f"The website added, {maxwebs} place left")
   
else:
    print("No available more entries")

# check list is not empty    

if len(myFavWeb) >0:
    myFavWeb.sort()
index = 0     


        
MyF = []
max_names = 4

while len(MyF) < max_names:
    name = input("Enter your friend's name: ").strip()

    # Check if the name is fully uppercase
    if name.isupper():
        print("Error! Invalid name (uppercase names are not allowed).")
    
    # If the name is in lowercase, capitalize the first letter and add it
    elif name.islower():
        MyF.append(name.capitalize())
        print(f"The first character of your friend's name {name} was capitalized.")
    
    # If the name is already properly formatted (capitalized), just add it
    elif name.capitalize() == name:
        MyF.append(name)
        print(f"Your friend {name} has been added.")
    
    else:
        print("Error! Invalid name format.")
    
    # Let the user know how many names can still be added
    print(f"You have {max_names - len(MyF)} names left.")

# After the loop finishes, print the full list of friends
print("No more names can be added.")
print("Friend list:", MyF)


#------------------------------<FOR>----------------------

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

# print(peoples['Osama'])

for name in peoples:
    print(f"Skills and Progress of {name} is: {peoples[name]}")
    
#------------------------------<Advanced Dict Loop>----------------------
    
myskills = {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%",
    'PHP' : '90%'
  }    
print(myskills.items())

for skills_key, skill_progress in myskills.items():
    
    print(f"{skills_key} ==> {skill_progress}")
    

myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}    
# loop on each key, value  
# loop on child key and its value 
for fkey, fvalue in myUltimateSkills.items():
    print(f"{fkey} ==> {fvalue}")
    for skey, svalue in fvalue.items():
        print(f"{skey} ==> {svalue}")