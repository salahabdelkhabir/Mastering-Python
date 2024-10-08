#----------------------------------------------------<1>----------------------------------------------------

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
      my_data.append(data[0])
      my_data.append(data[1])
      final_string = ''.join(my_data)
print(final_string) 

#----------------------------------------------------<2>----------------------------------------------------

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []
my_list3 = list(my_tuple)

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
      my_data.extend(my_list1[0:4])
      my_data.append(my_list3[2])
      my_data.append(my_list2[2])
      break  
  
final_string = ''.join(my_data) 
print(final_string)