# alien_color = 'green'
# if alien_color == 'green':
#     points = 5
# if alien_color == 'violet':
#     points = 10
# if alien_color == 'red':
#     points = 10
# print(f"You earned {points} for shooting alien")

# using else

# alien_color = 'red'
# alien_color = 'green'
alien_color = 'yellow'

if alien_color == 'green':
    points = 15
elif alien_color == 'red':
    points = 30
else:
    points = 20
print(f"You earned {points} for shooting alien!")