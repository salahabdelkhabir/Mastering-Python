# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re

is_email = re.search(r'[A-z0-9\.]+@[A-z0-9]+\.(com|net)', 'os@osama.com')
if is_email:
    print("This is valid email")
else:
    print("This is not valid email")    
print(is_email.span())
print(is_email.string)
print(is_email.group())

#--------------------------------------------------------------------------------------------------------------------

email = input("Enter your Email")
search = re.findall(r'[A-z0-9\.]+@[A-z0-9]+\.com|net', email)        
empty = []
if search != []:
    empty.append(search)
    print("Email added")
    
else:
    print("Invalid Email")    
    
for email in empty:
    print(email)