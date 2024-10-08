#----------------------------------------------------<1>----------------------------------------------------

my_nums = [15, 81, 5, 17, 20, 21, 13]
new = []
for i in my_nums:
      if i % 5== 0:
            new.append(i)

new.sort(reverse = True)
for a in range(len(new)):
  print(f"{a+1} ==> {new[a]}")
print("All numbers Printed")

#----------------------------------------------------<2>----------------------------------------------------

for i in range(20):
      if i <= 10:
            print(str(i).zfill(2))
      else:      
        print(i)

#----------------------------------------------------<3>----------------------------------------------------

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}     
ref = {
  'A' : 100, 
  'B': 80,
  'C' : 40
}
total_points = 0
for i, b in my_ranks.items():
      points = ref[b]
      total_points += points 
  
      print(f"My Rank in {i} Is {b} And This Equal {points} Points")
print(f"Total Points Is {total_points}")

#----------------------------------------------------<4-In traditional way>----------------------------------------------------

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

ref = {
  'A': 100, 
  'B': 80,
  'C': 40,
  'D': 20
}

for student, subjects in students.items():
    print("------------------------------")
    print(f"-- Student Name => {student}")
    print("------------------------------")
    
    total_points = 0
    
    for subject, rank in subjects.items():
        points = ref[rank]
        total_points += points
        print(f"- {subject} => {points} Points")
    
    print(f"Total Points For {student} Is {total_points}")

#----------------------------------------------------<4-Via .items()>----------------------------------------------------

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

ref = {
  'A': 100, 
  'B': 80,
  'C': 40,
  'D': 20
}

for student, subjects in students.items():
    print("------------------------------")
    print(f"-- Student Name => {student}")
    print("------------------------------")
    
    total_points = 0
    
    for subject, rank in subjects.items():
        points = ref[rank]
        total_points += points
        print(f"- {subject} => {points} Points")
    
    print(f"Total Points For {student} Is {total_points}")
