#  A list is a collection which is ordered and changeable. allows duplicate members

# Create list
nums = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'grapes']
#  use constructor
nums2 = list((1,2,3,4,5))

# get val
print(fruits[1])

# get length
print(len(fruits))

# Append to list
fruits.append('mangos')

#  remove from list
fruits.remove('grapes')

# change val
fruits[1] = 'grapes'

#  insert into pos
fruits.insert(2, 'bananas')

#  remove with pop
fruits.pop(2)

# reverse list
fruits.reverse()

# sort 
fruits.sort()

# reverse sort 
fruits.sort(reverse=True)
print( fruits)