#----------------------------------------------------<1>----------------------------------------------------

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

operations =input("Enter the mathematical operation tou need: ")

if operations =='+':
    num = num1 + num2
    print(f"The result is : [{num}]")
    
elif operations =='-':
    num = num1 - num2
    print(f"The result is : [{num}]")    

elif operations =='*':
    num = num1 * num2
    print(f"The result is : [{num}]")    

elif operations =='/':
    num = num1 / num2
    print(f"The result is : [{num}]")    
    
#----------------------------------------------------<2>----------------------------------------------------

print('-'*75)

age = 17
suitable = "The site is suitable for you" if age>16 else "The site is suitable for you"
print(suitable)    
print('-'*75)

#----------------------------------------------------<3>----------------------------------------------------

Age = int(input("Enter your Age: "))
months = Age * 12
days = months *30
weeks = days // 7
hours = days *24
minutes = hours *60
seconds = minutes *60
if Age>10 and Age<100:
    print(f"Years : [{Age}]")
    print(f"Months : [{months}]")
    print(f"Weeks : [{weeks}]")
    print(f"Days : [{days}]")
    print(f"Hours : [{hours}]")
    print(f"Minutes : [{minutes}]")
    print(f"Seconds : [{seconds}]")
else:
    print("Your age is out of acceptable range.")
    
#----------------------------------------------------<4>----------------------------------------------------

countries = {
    'Egypt': 0.7,
    'Saudia': 0.6,
    'Kuwait': 0.5,
    'Lybia': 0.4,
    'Arabic Emirates': 0.3,
    'Morroco': 0.2,
    'Algeria': 0.1
}
country = input("Enter your country: ").strip().capitalize()

if country in countries:
    price = 500
    discounts = price * countries[country]
    percentage = countries[country] *100

    
    print(f"Welcome of {country} people!\nwe have a surprise for you :\nYou have a great discount [{percentage}%] \nso The price will be [{discounts}] after it was [{price}]")
    
else:
    print("Sorry, There is no discount for you.")    