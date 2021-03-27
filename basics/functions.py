#  A function is a block of code that only runs when it is called, no braces uses indentation with tabs and spaces

# create func
def sayHello(name = 'Human Person'):
  print(f'Hello {name}')
  
sayHello('Bob')
sayHello()

# Return val
def getSum(num1, num2):
  total = num1 + num2
  return total

getSum(25, 5)

# A lambda function is a small anonymous func 
# lambda func can take any number of args, but can only have one expression

getNone = lambda num1, num2 : num1 - num2

none = getNone(10, 3)
print(none)