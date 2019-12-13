# Refactoring - is process of breaking code up into a series of functions that have a specific jobs.
# import json

# def greet_user():
#     """Greet user by name"""
#     filename = 'text_files/username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name?: ")
#         with open(filename, 'w') as f:
#             print(f"We will remember you when you are back, {username}!")
#     else:
#         print(f"Welcome back, {username}!")

#     greet_user()

import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'text_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name?: ")
    filename = 'text_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        check = input(f"Is username {username} is correct? y/n")
        if check == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = input("What is your name?: ")
            filename = 'text_files/username.json'
            with open(filename, 'w') as f:
                json.dump(username, f)
            return username
    else: 
        username = get_new_username()
        print(f"We will remember you when you are back, {username}!")

greet_user()