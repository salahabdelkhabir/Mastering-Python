#----------------------------------------------------<1>----------------------------------------------------

names = ['Youssef', 'Salah', 'Ashraf', 'Tarek', 'Abdelrahman' ]
print(names[0])
print(names.pop(0))

print(names[-1])
print(names.pop(-1))

print('--'* 50 )

#----------------------------------------------------<2>----------------------------------------------------

names = ['Youssef', 'Salah', 'Ashraf', 'Tarek', 'Abdelrahman' ]
print(names[0: :2])
print(names[1: :2])

print('--'* 50 )

#----------------------------------------------------<3>----------------------------------------------------

names_clone = names.copy()
print(names_clone[1:4])
print(names_clone[-2:])

print('--'* 50 )

#----------------------------------------------------<4>----------------------------------------------------

names[3] = 'Elzero'
names[4] = 'Elzero'
print(names)

print('--'* 50 )

#----------------------------------------------------<5>----------------------------------------------------

names.insert(0, "Samir")
names.append("Ahmed")
print(names)

print('--'* 50 )

#----------------------------------------------------<6>----------------------------------------------------

names.remove('Samir')
names.remove( 'Ahmed')
names.remove( 'Ashraf')
print(names)

print('--' * 50)

#----------------------------------------------------<7>----------------------------------------------------

employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

names.extend(employees)
names.extend(school)
print(names)
print('--'*50)

#----------------------------------------------------<8>----------------------------------------------------

names.sort(reverse=False)
print(names)
names.sort(reverse=True)
print(names)

print('--'*50)

#----------------------------------------------------<9>----------------------------------------------------

print(len(names))

print('--' *50)

#----------------------------------------------------<10>----------------------------------------------------

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][2])

print('--' *50)
