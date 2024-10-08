#----------------------------------------------------<1>----------------------------------------------------
print(bool("Salah"))
print(bool(5))
print(bool(10.59))
print(bool([1,2]))

#----------------------------------------------------<2>----------------------------------------------------

print(bool(0))
print(bool(None))
print(bool(""))
print(bool(False))

print('-' *75)

skill1 = {"Python": 90}
skill2 = {"C++": 70}
skill3 = {"Database": 80}
print(bool(skill1['Python'] > 50) and bool(skill2['C++'] > 50) and bool(skill3['Database'] > 50))

print('-'*75)

#----------------------------------------------------<3>----------------------------------------------------

num1 = 10
num2 = 20
num = 20
print(num > num1 or num > num2)
print(num > num1 and num > num2)
n1 = 10
n2 = 20
result = n1 + n2
print(result)
exp = result **3
print(exp)
mod = exp % 2600
print(mod)
print( mod / 5)
f = str(mod)
print(type(f))