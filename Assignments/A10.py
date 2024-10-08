#----------------------------------------------------<1>----------------------------------------------------

num = int(input("Enter a number"))

if num <= 0:
    print(f"Number {num} Is Not Larger Than 0")
else:
    count = 0
    for i in range(num - 1, 0, -1):
        if '6' not in str(i):
            print(i)
            count += 1
    print(f"{count} Numbers Printed Successfully.")
#----------------------------------------------------<2>----------------------------------------------------

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

ignored_count = 0
index = 0

while index < len(friends):
    if friends[index][0].islower():
        ignored_count += 1
    else:
        print(friends[index])
    index += 1

print(f"Friends Printed And Ignored Names Count Is {ignored_count}")

#----------------------------------------------------<3>----------------------------------------------------

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))

#----------------------------------------------------<4>----------------------------------------------------

my_friends = []
max_friends = 4

while len(my_friends) < max_friends:
    name = input().strip()

    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        name = name.capitalize()
        my_friends.append(name)
        print(f"Friend {name} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {max_friends - len(my_friends)}")
    else:
        my_friends.append(name)
        print(f"Friend {name} Added")
        print(f"Names Left in List Is {max_friends - len(my_friends)}")
