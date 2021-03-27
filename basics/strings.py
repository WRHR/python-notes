# strings in python are surrounded by either single or double quotes

name = 'Joe'
age = 31

#Concat
# print('Hello my name is '+ name + ' and I am '+ str(age))

# String Formatting

#Args by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings
print(f'Hello, My name is {name} and I am {age}')

# String Methods

s = 'hello world'

# capitalize string
print(s.capitalize())

print(s.upper())
print(s.lower())

print(s.swapcase())

#get length
print(len(s))

# Replace 
print(s.replace('hello', 'goodbye'))

# count 
sub_string = 'h'
print(s.count(sub_string))

# starts with ->bool
print(s.startswith('hello'))

# ends with -> bool
print(s.endswith('d'))

# find position
print(s.find('r'))

# Spilt 
print(s.split())

# is all alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())

