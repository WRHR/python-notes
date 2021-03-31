# If/else conditionals
x = 10
y = 5

# if x > y:
#   print(f'{x} is greater than {y}')

# else:
#   print(f'{x} is less than {y}')

if x > y:
  print(f'{x} is greater than {y}')

elif x == y:
  print(f'{x} is equal to {y}')

else:
  print(f'{x} is less than {y}')

# nested

if x > 2:
  if x <= 10:
    print("Hello from the nest")

# Logical operators (and , or, not)
if x > 2 and x > 5:
  print(f'{x} is greater than 5 and 2')


numbers = [1,2,3,4,5,10]

if x in numbers:
  print(x in numbers)

# is 

if x is not y:
  print(x is y)