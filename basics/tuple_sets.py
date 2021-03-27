#  A Tuple is a collection which is ordered and unchangeable. allows duplicate members

# create tuple
fruits = ('apples', 'oranges', 'grapes')

# constructor
# fruits2= tuple(('apples', 'pears', 'watermelon'))

# get val
print(fruits[1])

# cant change val
# fruits[0] = 'whatever'

# delete tuple 
# del fruits2

print(fruits)


# A set is a collection which is unordered and unindexed. no duplicate members

veg = {'tomatoes', 'lettuce', 'kale'}

# check if in set
print('kale' in veg)

#  add to set
veg.add('cucumber')

#  remove from set
veg.remove('tomatoes')

#  clear set
veg.clear()

#  delete
del veg

print(veg)