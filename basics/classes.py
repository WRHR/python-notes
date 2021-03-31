# Classes 

# create
class User:
  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def addDecade(self):
    self.age += 10
  
# Init user object

# dude = User('Some Guy', 25)
# dude.addDecade()
# print(dude.age)

# extend class 

class Customer(User):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

sue = Customer('Sue', 29)

sue.set_balance(500)
sue.addDecade()

print(f'{sue.name} has ${sue.balance} and is now {sue.age}')