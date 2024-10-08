#----------------------------------------------------<1>----------------------------------------------------

class Game:
    def __init__(self, name, developer,year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
    
    def price_in_pounds(self):
        return self.price * 15.6       

game_one = Game("Ys", "Falcom", 2010, 50)   

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()} Egyptian Pounds", end="")

#----------------------------------------------------<2>----------------------------------------------------

class User:
    def __init__(self, FName, LName, age, gender):
        self.FName = FName
        self.LName = LName
        self.age = age
        self.gender = gender

    def full_details(self):
        title = "Mr" if self.gender == "Male" else "Mrs"
        years_to_40 = 40 - self.age
        return f"Hello {title} {self.FName} {self.LName[0]}. [{years_to_40:02}] Years To Reach 40"

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())
print(user_two.full_details())

#----------------------------------------------------<3>----------------------------------------------------

class Message:
    def __init__(self) :
        pass
    @staticmethod
    def print_message():
        return "Hello From Class Message"
    
print(Message.print_message())

#----------------------------------------------------<4>----------------------------------------------------

class Games:
    def __init__(self, input_data):
        self.input_data = input_data
    
    def show_games(self):
        if isinstance(self.input_data, str):  
            return f"I Have One Game Called \"{self.input_data}\""
        elif isinstance(self.input_data, list):  
            games_list = "\n".join([f"-- {game}" for game in self.input_data])
            return f"I Have Many Games:\n{games_list}"
        elif isinstance(self.input_data, int):  
            return f"I Have {self.input_data} Game{'' if self.input_data == 1 else 's'}."
        else:
            return "Invalid input"

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

print(my_game.show_games())
print(my_games_names.show_games())
print(my_games_count.show_games())

#----------------------------------------------------<5>----------------------------------------------------

# Main Class
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

class Admins(Members):
    pass
    
class Moderators(Members):
    
    def __init__(self, n, p):
    
      super().__init__(n,p)

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
print(member_two.show_info())

#----------------------------------------------------<6>----------------------------------------------------

class A:
    def __init__(self, one):
        self.one = one

class B:
    def __init__(self, two):
        self.two = two

class C:
    def __init__(self, three):
        self.three = three

class Name(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)
    
    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"


the_name = Name("El", "ze", "ro")

print(the_name.show_name())

