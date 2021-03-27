#A variable is a container for a value

'''
Doc strings
Multi line comment
'''

"""
Var rules:
  -Var names are case sensitive 
  -Must start w/ letter or _
  -Can have num but not at start
"""

# x = 1         #Cast as int

# y = 2.5       #Float

# name = 'Joe'  #str

# is_cool = True #bool

#multiple assignment
x, y, name, is_cool = (1,2.5, 'John', True)

x =str(x)
y = int(y)

print('hello')
print(type(x))