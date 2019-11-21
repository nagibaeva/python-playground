# Dictionaries.
# To store variable and their values in a dictionary use    dictionary = {'variable' : 'value'}
# Dictionary = {'key' : 'value'}    ,where value can be as a form of string, number, list or other dictionary.
# To access the value use []

alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

points = alien_0['points']
print(f"You have earned {points} points!")

# To add new key-value pair:    Dictionary['key'] = 'value'

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# You can assign new value to the keys of dictionaries:

print(f"\nThe alien color was {alien_0['color']}.")

alien_0['color'] = 'red'
print(f"Now the color of alien is {alien_0['color']}.")

# Ex with alien speed

alien_1 = {'x_position':0, 'y_position':25, 'speed': 'medium'}
print(f"\nStarting position of alien is {alien_1['x_position']} with {alien_1['speed']} speed.")
#Now move alien to the right at a given speed.

if alien_1['speed'] == 'slow':
    x_movement = 1
elif alien_1['speed'] == 'medium':
    x_movement = 2
else:
    x_movement = 3

# Now show new position of alien:

alien_1['x_position'] = alien_1['x_position'] + x_movement

print(f"\nNow new position of alien is {alien_1['x_position']}.\n")

# To remove key-value pair from dictionary use: del dictionary['key']
# Note: key-value pair will be removed permanently and will not be accecable.

print("Features of alien_0:")
print(alien_0)

del alien_0['points']
print("\nFeatures of alien_0 after key (points) was removed:")
print(alien_0)

# Use dictionary to store one kind of info about many objects.
# Note: To use separate lines for each key-value pair, after opening {  press enter

best_languages = {
    'sam' : 'python',
    'luke' : 'java',
    'dan' : 'ruby',
    'mary' : 'c',
}

print(f"\nDan prefers using {best_languages['dan'].title()}.\n")

# In case if the key you are asking is absent, you may use get() method:

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#Note: get() method gives opportunity in case if key is absent in the 
# dictionary to show that the value is absent. (similar to if then function of excel)
