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

dude = User('Some Guy', 25)
dude.addDecade()
print(dude.age)


