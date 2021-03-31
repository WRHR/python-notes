# a module is a file containing a set functions to include in your app. there are core modules available in pip package manager

# core modules
import datetime
from datetime import date
import time
from time import time

#pip modules
from camelcase import CamelCase

today = date.today()
# today = datetime.date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello world'))

print(timestamp)

