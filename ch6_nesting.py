# Nesting is storgae of multiple dictionraies in a list, or list as a value in a dictionary, or dictionaries in a dictionary.

# List of a dictionaries

alien_0 = {'color' : 'green', 'points': 5}
alien_1 = {'color' : 'yellow', 'points': 10}
alien_2 = {'color' : 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

for alien in aliens:
    for color, points in alien.items():
        print("\n")
        print(color.title())
        print(points)

# Ex how to generate 30 identical dictionaries:

# Make empty list:
aliens =[]

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created:
print(f"Total number of aliens: {len(aliens)}")

# List in a Dictionary

# Create dictionary     pizza   to store the information
pizza = {
    'crust' : 'thick',
    'toppings' : ['musrooms', 'extra cheese'],
}

# Summarize the order
print(f"\nYou ordered a {pizza['crust']} crust pizza with follofing toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
# Note: to get list of toppings in pizza we used command    for key in dictionary['keys']:

# Example with favorite languages:

best_languages = {
    'sam' : ['python', 'c'],
    'luke' : 'go',
    'dan' : ['ruby', 'python'],
    'mary' : 'c++',
    'rem' : ['c+', 'ruby'],
}

# To get list as value for each jey use for command in for command:

for name, languages in best_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Dictionary in a Dictionary

# Ex: dictionary    users   with keys as    username    and corresponding values as dictionary of information about users

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstien',
        'location' : 'princeton',
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
