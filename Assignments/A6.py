#----------------------------------------------------<1>----------------------------------------------------

l = [1,2,3,3,4,5,1]
unique_list = [1,2,3,4,5]
print(unique_list)
print(type(unique_list))
unique_list.pop()
print(unique_list)

print('--'*50)

#----------------------------------------------------<2>----------------------------------------------------

nums = {1,2,3}
let = {"A", "B", "C"}

#2.1
print( nums | let)
#2.2
b = nums.union(let)
print(b)
#2.3
nums.update(let)
print(nums)

print('--'*50)

#----------------------------------------------------<3>----------------------------------------------------

#3.1
my_skills_set = {1,2,3}
print(my_skills_set)
#3.2
my_skills_set.clear()
print(my_skills_set)
#3.3
my_skills_set.add('A')
my_skills_set.add('B')
print(f"{my_skills_set}")
#3.4
my_skills_set.discard('C')
print(my_skills_set)

print('--'*50)

#----------------------------------------------------<4>----------------------------------------------------

set1 = {1,2,3}
set2 = {1,2,3,4,5,6}
print(set1.issubset(set2))

print('--'*50)

#----------------------------------------------------<5>----------------------------------------------------

my_skills = {"HTML":"90%",
      "Python": "100%",
      "CSS": "80%",
      "JAVA":"60"}


print(f"Python progress is {my_skills['Python']}")
print(f"HTML progress is {my_skills['HTML']}")
print(f"CSS progress is {my_skills['CSS']}")
print(f"JAVA progress is {my_skills['JAVA']}")
my_skills.update({"Database": "95%"})
print(my_skills)

print('--'*50)
