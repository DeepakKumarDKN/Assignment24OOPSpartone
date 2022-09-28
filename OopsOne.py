# 1. Write a python program to create a user class with 3 properties : name, age, email.

'''
class User:
  def __init__(self,name,age,email):
    self.name = name
    self.age = age
    self.email = email

user= User('deepak',22,'deepakflushymax@gmailcom')
print(user.name,user.age,user.email,sep="\n")

'''


# 2. Write a python program to create a user class with a method to greet the user.
'''
class User:
  def __init__(self,name,age,email):
    self.name = name
    self.age = age
    self.email = email
  def greetUser(self):
    print('Hi {} GoodMorning how are you'.format(self.name))

user= User('deepak',22,'deepakflushymax@gmailcom')
user.greetUser()
'''
# 3. Write a python program to create 2 objects of the user class and assign different values.
'''
class User:
  def __init__(self,name,age,email):
    self.name = name
    self.age = age
    self.email = email

userOne= User('deepak',22,'deepakflushymax@gmailcom')
userTwo = User('Reyansh',22,'reyansh@gmail.com')

print(userOne.name, userOne.age, userOne.email, sep="\n")
print()
print(userTwo.name, userTwo.age, userTwo.email, sep="\n")

'''
# 4. Write a python program to init default values for user object using __init__ method.
'''
class User:
  def __init__(self,name,age,email="deepak@gmail.com"):
    self.name = name
    self.age = age
    self.email = email
  def displayUserInfo(self):
    print(self.name,self.age,self.email,sep="\n")

user = User('Deepak',22)
user.displayUserInfo()
'''
# 5. Write a python program to delete the age property of the user.
'''
class User:
  def __init__(self,name,age,email="deepak@gmail.com"):
    self.name = name
    self.age = age
    self.email = email
  def displayUserInfo(self):
    print(self.name,self.age,self.email,sep="\n")

user = User('Deepak',22)
user.displayUserInfo()
del user.name
print(user.__dict__)
'''

# 6. Write a python program to create 3 user objects and find the youngest of all.
'''
class User:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
  @staticmethod
  def displayYounger(a,b,c):
    print('youngest is', a.name  if(a.age<b.age and a.age<c.age) else b.name 
    if(b.age<a.age) and b.age<c.age else c.name)

userOne = User('deepak',22)
userTwo = User('Rahul',14)
userThree = User('Ravi',18)
User.displayYounger(userOne,userTwo,userThree)
'''


# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
# values).

class Laptop:
  def __init__(self,brand,ram,cpu,hdd):
    self.brand = brand
    self.ram = ram
    self.cpu = cpu
    self.hdd = hdd

  def showConfig(self):
    print(self.brand, self.ram,self.cpu,self.hdd, sep="\n")
  
  def showConfig(self):
    print('Laptop brand name is:', self.brand)
    print('Laptop ram is:', self.ram,'gb')
    print('Laptop cpu name is:', self.cpu)
    print('Laptop hdd name is:', self.hdd)


laptop = Laptop('Lenevo',16,'Intel Core i7','SATA')
laptop.showConfig()



# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.

# class Laptop:
#   def __init__(self,brand,ram,cpu,hdd):
#     self.brand = brand
#     self.ram = ram 
#     self.cpu = cpu
#     self.hdd = hdd
  
#   def addLaptops():
#     pass
    
# laptopOne = Laptop('Lenevo',16,'Intel Core i7','SATA')
# laptopTwo = Laptop('HP',28,'Intel Core i9','SSD')
# laptopThree = Laptop('Dell',32,'Intel Core i5','NVMe')

# Laptop.addLaptops()



# 9. Write a python program to create a School class and 3 instance variables and 1 class
# variable.
'''
class School:
  scholName = "Ineuron"

  def __init__(self,course,fees,teacher):
    self.course = course
    self.fees = fees
    self.teacher = teacher 
  
schooldata = School('Python Fullstack',4000,['Saurabh Shukla','Naveen Sir'])
print(schooldata.course, schooldata.fees, schooldata.teacher,sep="\n")
'''

# 10. Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values
'''
class Employee:
  def __init__(self,empid,name,salary):
    self.empid = empid
    self.name = name
    self.salary = salary
  
  def displayEmployeeData(self):
    print('Employee Id is:',self.empid)
    print('Employee name is:', self.name)
    print('Employee salary is:', self.salary)

employee = Employee(190988,'Rahul Krishna Vaidya',12000)
employee.displayEmployeeData()

'''
