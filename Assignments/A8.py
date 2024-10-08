#----------------------------------------------------<1>----------------------------------------------------

name = input(("Enter your name "))
name = name.strip(' ')
name = name.capitalize()
print(f"Hello {name}, Happy To See You Here.")    
print('-*50')

#----------------------------------------------------<2>----------------------------------------------------

age = input("Please enter your age.")
age = int(age)
if age<16:
    print("Sorry, This site is not suitable for you.")
else:
    print("Good, This site is suitable for you.")
        
print('-*50')

#----------------------------------------------------<3>----------------------------------------------------

first_name =input(("Enter your First name"))
second_name =input(("Enter your Second name"))

name = first_name.strip(' ')
name = second_name.strip(' ')
name = second_name.capitalize()
name = second_name.capitalize()
print(f"Welcome Mr {first_name} {second_name[0]}.")

print('-*50')

#----------------------------------------------------<4>----------------------------------------------------

email = input("Enter your E-mail: ")
email = email.strip(' ')
email = email.lower()
name_email = email[:email.index('@')]
name_email = name_email.capitalize()
print(f"{name_email}")
site = email[email.index('@') +1 :email.index('.')]
domain = email[email.index('.') +1 :]
print(f"Your Name : {name_email}")
print(f"Your Site : {site}")
print(f"Your Domain : {domain}")
print('-*50')
