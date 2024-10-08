#----------------------------------------------------<1>----------------------------------------------------


def remove_chars(string):
    return string[1:-1]  

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list:
    print(name)  

for name in map(lambda x: x[1:-1], friends_map):
    print(name)  

#----------------------------------------------------<2>----------------------------------------------------


def get_names(name):
    return name.endswith('m') 

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)

for name in names:
    print(name)  

for name in filter(lambda x: x.endswith('m'), friends_filter):
    print(name)  


#----------------------------------------------------<3>----------------------------------------------------


from functools import reduce

def multiply(x, y):
    return x * y

nums = [2, 4, 6, 2]

result = reduce(multiply, nums)
print(result)  

result_lambda = reduce(lambda x, y: x * y, nums)
print(result_lambda)  

#----------------------------------------------------<4>----------------------------------------------------


skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

index = 50
for i in range(len(skills) - 1, -1, -1):  
    if isinstance(skills[i], str):  
        print(f"{index} - {skills[i]}")
    index += 1
