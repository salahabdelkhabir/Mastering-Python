import re

my_string = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

result = re.findall(r"(\w )", my_string)

print(result)

#----------------------------------------------------<1>----------------------------------------------------

import re

my_string = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

result = re.findall(r"(L[A-z]+)", my_string)

print(result)

#----------------------------------------------------<2>----------------------------------------------------

import re

my_string1 = "+(0100) 600-1234"
my_string2 = "+(0100) 60-1234"
my_string3 = "(0100) 6000-1234"
my_string4 = "01006001234"
my_string5 = "0100 600 1234"
my_string6 = "(0100) 600-1"
my_string7 = "(0100) 600-12"


result1 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string1)
result2 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string2)
result3 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string3)
result4 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string4)
result5 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string5)
result6 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string6)
result7 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string7)

#----------------------------------------------------<3>----------------------------------------------------

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)


#----------------------------------------------------<4>----------------------------------------------------


import re

my_string1 = "http://www.elzero.org:8888/link.php"
my_string2 = "https://elzero.org:8888/link.php"
my_string3 = "http://www.elzero.com/link.py"
my_string4 = "https://elzero.com/link.py"
my_string5 = "http://www.elzero.net"
my_string6 = "https://elzero.net"

result1 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string1)
result2 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string2)
result3 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string3)
result4 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string4)
result5 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string5)
result6 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string6)


print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)

#----------------------------------------------------<5>----------------------------------------------------

import re

my_string = "http || https || abcd || abcd"

result = re.findall(r"(http\w?)", my_string)

print(result)
