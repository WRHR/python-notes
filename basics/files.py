# Files in python, can CRUD files

# Open a file

myFile = open('myfile.txt', 'w')

# Get some info 
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Mode: ', myFile.mode)

# Write to file
myFile.write('I love python')
myFile.write(' and Javascript')

myFile.close()

# Append to file 
myFile = open('myfile.txt', 'a')
myFile.write(' I love it all')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)