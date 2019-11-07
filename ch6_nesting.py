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