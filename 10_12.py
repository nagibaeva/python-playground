# Favorite numbers remembered

import json

filename = 'text_files/favorite_number.json'
try:
    with open(filename) as f:
        user_number = json.load(f)
except FileNotFoundError:
    user_number = input("What is your favorite number?: ")
    with open(filename, 'w') as f:
        json.dump(filename, f)
        print(f"We will remember your favorite number is {user_number}!")
else:
    print(f"Your favorite numbers is {user_number}!")