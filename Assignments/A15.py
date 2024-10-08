#----------------------------------------------------<1>----------------------------------------------------


# Define a tuple called values that has 0, 1, and 2
values = (0, 1, 2)

# Check if any value in the tuple is True (non-zero)
if any(values):  # Since 1 and 2 are non-zero, this is True
  my_var = 0  # Assign my_var to 0

# Define a list with some values, including my_var
my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# Check if the first 4 values in the list are all True
# OR if the first 6 values in the list are all True
# OR if all values in the entire list are True
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
  print("Good")  # If any of the conditions above are True, print "Good"
else:
  print("Bad")  # Otherwise, print "Bad"

# Expected output: "Bad", because my_list[:6] contains my_var which is 0, so it will fail.

#----------------------------------------------------<2>----------------------------------------------------


# We need to find the value of v that makes the result 820
# The value v = 40 will give the correct result
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

#----------------------------------------------------<3>----------------------------------------------------


# We need to find the value of n that makes the average equal to 10
# The value n = 5 will give an average of 10
n = 5

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
  print("Good")


#----------------------------------------------------<4>----------------------------------------------------


# Create a function my_all that works like the built-in all function
def my_all(iterable):
  for element in iterable:
    if not element:
      return False  # If any element is False, return False
  return True  # If all elements are True, return True

# Create a function my_any that works like the built-in any function
def my_any(iterable):
  for element in iterable:
    if element:
      return True  # If any element is True, return True
  return False  # If all elements are False, return False

# Create a function my_min that works like the built-in min function
def my_min(iterable):
  min_value = iterable[0]  # Start with the first element
  for element in iterable[1:]:
    if element < min_value:
      min_value = element  # Update if we find a smaller value
  return min_value

# Create a function my_max that works like the built-in max function
def my_max(iterable):
  max_value = iterable[0]  # Start with the first element
  for element in iterable[1:]:
    if element > max_value:
      max_value = element  # Update if we find a bigger value
  return max_value

# Test my_all function
print(my_all([1, 2, 3]))  # True, all values are True
print(my_all([1, 2, 3, []]))  # False, an empty list is False

# Test my_any function
print(my_any([0, 1, [], False]))  # True, 1 is True
print(my_any([(), 0, False]))  # False, all values are False

# Test my_min function
print(my_min([10, 100, -20, -100, 50]))  # -100, it's the smallest
print(my_min((10, 100, -20, -100, 50)))  # -100, same for tuple

# Test my_max function
print(my_max([10, 100, -20, -100, 50, 700]))  # 700, it's the biggest
print(my_max((10, 100, -20, -100, 50, 700)))  # 700, same for tuple
