#----------------------------------------------------<1>----------------------------------------------------

from datetime import datetime

start_date = datetime(2021, 6, 25)
end_date = datetime.now()

delta = end_date - start_date
days_difference = delta.days

print(f"Days From {start_date.strftime('%Y-%m-%d')} To {end_date.strftime('%Y-%m-%d')} Is => {days_difference}")

#----------------------------------------------------<2>----------------------------------------------------


from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))                     
print(now.strftime("%b %d, %Y"))                 
print(now.strftime("%d - %b - %Y"))                  
print(now.strftime("%d / %b / %y"))                 
print(now.strftime("%d / %B / %Y"))                  
print(now.strftime("%a, %d %B %Y"))                  
