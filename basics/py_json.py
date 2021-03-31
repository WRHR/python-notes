# JSON

import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name":"Smith", "age": 30}'

user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make':'Ford', 'model':'Mustange', 'year':1970}

carJSON = json.dumps(car)

print(carJSON)