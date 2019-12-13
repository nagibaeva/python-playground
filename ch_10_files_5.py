# Storing data using JSON module
# JSON is JavaScript Object Notation

# json.dump() module stores set of data. Two arguments are needed for json.dump() module: piece of data to be stored and a file object where to store the data.

import json

numbers = [2, 3, 5, 7, 9, 11, 13]
filename = 'text_files/numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

# json.load() module reads the data back into memory. One argument is needed: file object from where to read the data.

import json    

filename = 'text_files/numbers.json'
with open(filename) as f:
    read_numbers = json.load(f)

print(read_numbers)

# Saving and Reading the user generated data

import json

username = input("What is your name?: ")

filename = 'text_files/username.json'
with open(filename,'w') as f:
    json.dump(username, f)
    print(f"We will remember you when you come back, {username}!")

import json
filename = 'text_files/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

# For the combined version please see remember_me.py

