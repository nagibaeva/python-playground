# Favorites numbers
import json

number = input("What is your favorite number?: ")
filename = 'text_files/favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
with open(filename) as f:
     user_number = json.load(f)
     print(f"Now we know your favorite number is {user_number}!")