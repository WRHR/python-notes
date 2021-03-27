# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members

# create dictionary
person = {
  'first_name':'John',
  'last_name':'Smith',
  'age':29
}

# constructor
person2 = dict(first_name='Sally', last_name= 'Sanders')

# get val
print(person['age'])

print(person.get('first_name'))

# add key val
person['phone']= '555-555-5555'

# get all keys
print(person.keys())

#  get items
print(person.items())

#  copy dict
person3 = person.copy()
person3['city'] = 'NYC'

print(person3)
# Remove item
del(person['age'])

person.pop('phone')

# clear 
person.clear()

# get length
print(len(person3))

# list of dictionaries
people = [
  {'name':'Martha', 'age':30},
  {'name':'Clark', 'age':10}
]

print(people[0]['age'])

print(person)
