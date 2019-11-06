# Dictionaries

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'Congratulations! You have earned {new_points} points!')

# Adding new key-value pairs to the dictionary

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Adding key-value pairs to empty dictionary

alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10

print(alien_1)

# Modifying the value of keys in dictionaries

print(f"\nThe color of alien is {alien_1['color']}")

alien_1['color'] = 'yellow'
print(f"The new color of alien is {alien_1['color']}")
