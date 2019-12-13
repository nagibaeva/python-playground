import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'text_files/username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?: ")
    with open(filename, 'w') as f:
        json.dump(filename, f)
        print(f"We will remember you when you are back, {username}!")
else:
    print(f"Welcome back, {username}!")