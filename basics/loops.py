#  A for loop is used for iterating over a squence (that is either a list, tuple, dictionary, set or a string)

people = ['Joe', 'Poe', 'Moe']

# # simple
# for person in people:
#   print(f'Current Person: {person}')

# # break
# for person in people:
#   if person == 'Poe':
#     break
#   print(f'Hello my name is {person}')

# continue
# for person in people:
#   if person == 'Poe':
#     continue
#   print(f'Hey {person}')

# range
for i in range(len(people)):
  print(f'{i+1}: {people[i]}')

# while loops execute a set of statments 

count = 0

while count <=10:
  print(f'Count: {count}')
  count +=1

