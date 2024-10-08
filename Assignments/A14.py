#----------------------------------------------------<1>----------------------------------------------------

import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder = os.path.join(desktop_path, "Python")

if not os.path.exists(python_folder):
    os.makedirs(python_folder)

assign_file = os.path.join(python_folder, "assign.py")
with open(assign_file, 'w') as f:
    pass

for i in range(1, 51):
    if i == 25:
        filename = "special-text.txt"
        with open(os.path.join(python_folder, filename), 'w') as f:
            pass
    else:
        filename = f"txt{i}.txt"
        with open(os.path.join(python_folder, filename), 'w') as f:
            f.write(f"Elzero Web School => {i}\n")

print(os.getcwd())
print(python_folder)
print(os.path.basename(assign_file))
print(len([f for f in os.listdir(python_folder) if f.endswith('.txt')]))

#----------------------------------------------------<2>----------------------------------------------------

txt1_file = os.path.join(python_folder, "txt1.txt")

with open(txt1_file, 'a') as f:
    for _ in range(50):
        f.write("Appended => Elzero Web School\n")
        
#----------------------------------------------------<3>----------------------------------------------------

with open(txt1_file, 'r') as f:
    lines = f.readlines()

number_of_lines = len(lines)
number_of_words = sum(len(line.split()) for line in lines)
number_of_chars = sum(len(line) for line in lines)
number_of_l = sum(line.count('l') for line in lines)

print(f"Number Of Lines Is => {number_of_lines}")
print(f"Number Of Words Is => {number_of_words}")
print(f"Number Of Chars Is => {number_of_chars}")
print(f"Number Of 'l' Char Is => {number_of_l}")

#----------------------------------------------------<4>----------------------------------------------------

txt_files = [f for f in os.listdir(python_folder) if f.startswith('txt') and f.endswith('.txt')]

txt_files.sort(reverse=True)
for file in txt_files[:10]:
    os.remove(os.path.join(python_folder, file))
