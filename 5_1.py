plants = ['lily', 'begoni','astra','rose']
for plant in plants:
    if plant == 'rose':
        print("True")
    else:
        print("False")
for plant in plants:
    if plant == 'rose':
        print("\nYes")
else:
    print('\nNo')
for plant in plants:
    if plant != 'rose':
        print(plant.upper())
    else:
        print(plant.title())
if 'rose' in plants:
    print("\nIncluded")
else:
    print("Not Included")

if 'rose' not in plants:
    print('\neliminated')
else:
    print("\nShould be removed")