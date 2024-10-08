#----------------------------------------------------<Map>----------------------------------------------------
# Can be with pre-defined function or lambda
#accept functiond + iterable

def format_text(text):
    return f"- {text} -"

myTexts = ['Osama', 'Ahmed', 'Sayed']
Format_Data = map(lambda text: f"- {text} -" , myTexts)
print(Format_Data)

for name in Format_Data:
    print(name)
    
#----------------------------------------------------<Filter>----------------------------------------------------
# Can be with pre-defined function or lambda
# Accepts functiond + iterable
# Executes (filters) only true values

#----------------------------------------------------<ٌReduce>----------------------------------------------------

# Apply function in the first two elements to generate one element (Result).

from functools import reduce  

def sumAll(num1, num2):
    return num1 + num2
numbers = [1, 8, 2, 9, 100]
result = reduce(sumAll, numbers)
print(result)  #120

#----------------------------------------------------<Enumerate>----------------------------------------------------
# enumerate(iterable, start = 0)
mySkills = ['HTML', 'CSS', 'JS', 'PHP']

mySkillsWithCounter = enumerate(mySkills,20)
print(type(mySkillsWithCounter))
for c, skill in mySkillsWithCounter:
    print(f'{c} - {skill}')
    
#----------------------------------------------------<Help>----------------------------------------------------
# Get info for any function
print(help(print))

#----------------------------------------------------<Reversed>----------------------------------------------------
country = 'Egypt'
for c in reversed(country):
    print(c)