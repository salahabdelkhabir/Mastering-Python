#----------------------------------------------------<OOP>----------------------------------------------------


# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object



#----------------------------------------------------<Class Syntax>----------------------------------------------------

# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function

class membersMembers:
        
    
    def __init__(self):
        
        print("A New mamber has been Added")
        
print(dir(membersMembers))
membersMembers_one = membersMembers()
membersMembers_two = membersMembers()
membersMembers_three = membersMembers()
print(membersMembers_one.__class__)


#----------------------------------------------------<Instance Attributes & Methods Syntax>----------------------------------------------------

# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------------------

class Members:
    
    def __init__(salah, FName, MName, LName, Age, title) :
        
        salah.fname = FName
        salah.mname = MName
        salah.lname = LName
        salah.age = Age
        salah.title = title
    
    def fullName(salah):
        return f"{salah.fname} {salah.mname} {salah.lname}"
    
    def Hello(salah):
        salah.title = input("Please Inter Your Title Job ")
        return f"Hello, {salah.title} {salah.fname}"

membersMembers_one = Members("Salah", 'Gamal', 'Abdelkhabir',21,'Eng.')
membersMembers_two = Members("Youssef", 'Hatem', 'Motawea', 20, 'Dr.')
membersMembers_three = Members("Ahmed", 'Elsayed', 'Abdelsalam', 20, 'Dr.')
        
print(membersMembers_one.Hello())

#----------------------------------------------------<Class Attributes & Methods Syntax>----------------------------------------------------
# Outside the Constructor
class Members:
    
    #Class Attribute => Outside constructor
    
    not_allowed_names = ['Hell', 'Shit', 'Shatup']
    users_conut = 0
    
    def __init__(self, FName, MName, LName, Age, title) :
        
        
        self.fname = FName
        self.mname = MName
        self.lname = LName
        self.age = Age
        self.title = title
        Members.users_conut += 1 
    
    def fullName(self):
        
        if self.fname in Members.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:
            return f"{self.fname} {self.mname} {self.lname}"
    
    def Hello(self):
        self.title = input("Please Inter Your Title Job ")
        return f"Hello, {self.title} {self.fname}"
    
    def delete_user(self):
        Members.users_conut -= 1
        return f"User {self.fname} Deleted."
print(Members.users_conut)
membersMembers_one = Members("Shit", 'Gamal', 'Abdelkhabir',21,'Eng.')
membersMembers_two = Members("Youssef", 'Hatem', 'Motawea', 20, 'Dr.')
membersMembers_three = Members("Ahmed", 'Elsayed', 'Abdelsalam', 20, 'Dr.')
membersMembers_Four = Members("Shit", 'Hell', 'Shatup', 20, 'Dr.')
membersMembers_Four.delete_user()            
print(Members.users_conut)
print(membersMembers_one.fullName())

#----------------------------------------------------<Class Methods & Static Methods>----------------------------------------------------


#----------------------------------------------------<1-Class Methods>----------------------------------------------------


# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself


class Members:
    
    
    not_allowed_names = ['Hell', 'Shit', 'Shatup']
    users_conut = 0
    
    # Class Method
    
    @classmethod
    def show_users_count(cls):
        print(f"We have {cls.users_conut} Users in Our System")

 
    def __init__(self, FName, MName, LName, Age, title) :
        
        
        self.fname = FName
        self.mname = MName
        self.lname = LName
        self.age = Age
        self.title = title
        Members.users_conut += 1 
    
    def fullName(self):
        
        if self.fname in Members.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:
            return f"{self.fname} {self.mname} {self.lname}"
    
    def Hello(self):
        self.title = input("Please Inter Your Title Job ")
        return f"Hello, {self.title} {self.fname}"
    
    def delete_user(self):
        Members.users_conut -= 1
        return f"User {self.fname} Deleted."
    
Members_one = Members("Salah", 'Gamal', 'Abdelkhabir',21,'Eng.')
Members_two = Members("Youssef", 'Hatem', 'Motawea', 20, 'Dr.')
Members_three = Members("Ahmed", 'Elsayed', 'Abdelsalam', 20, 'Dr.')
Members_Four = Members("Shit", 'Hell', 'Shatup', 20, 'Dr.')
Members_Four.delete_user()            
print(Members.users_conut)
Members.show_users_count()


#----------------------------------------------------<2- Static Methods>----------------------------------------------------

# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class


class New:
    
    not_allowed_names = ['Hell', 'Shit', 'Shatup']
    users_conut = 0
    
    #Static Method

    @staticmethod
    def say_hello():
        print("This is a Static Method")    
        
New.say_hello()        
#----------------------------------------------------<Magic Methods>----------------------------------------------------

# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
# Called When We Use the Built-in len() Function on the Object

class Skill:
    
  def __init__(self):

    self.skills = ["Html", "Css", "Js"]

  def __str__(self):

    return f"This is My Skills => {self.skills}"

  def __len__(self):

    return len(self.skills)

profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))

print(profile.__class__)
my_string = "Osama"
print(type(my_string))
print(my_string.__class__)
print(dir(str))
print(str.upper(my_string))