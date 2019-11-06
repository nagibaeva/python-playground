alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print('\nYou earned 5 points!')
if 'violet' in alien_colors:
    print('\nYour earned 1 point!')

for alien_color in alien_colors:
    if alien_color == 'green':
        print("\nYou did a great job!")
    elif alien_color == 'yellow':
        print('You almost did it!')
    else:
        print("Try one more time!")

items = []
if items:
    for item in items:
        print("\nAdding choosen {item} to the cart!")
else:
    print("\nAre you sure you want to proceed to the cart?")

available_names = ['jhon', 'jackie', 'jordan', 'james', 'jerome']
requested_names = ['jackie', 'jane', 'jordan']
for requested_name in requested_names:
    if requested_name in available_names:
        print(f"\nCongratulations! The name {requested_name.title()} is available!")
    else:
        print("\nSorry, given name is not available.")
