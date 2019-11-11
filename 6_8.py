pets = []

pet = {
    'name' : 'roksi',
    'type' : 'cat',
    'owner' : 'pana',
}
pets.append(pet)

pet = {
    'name' : 'eshka',
    'type' : 'cat',
    'owner' : 'akin',
}

pets.append(pet)

pet = {
    'name' : 'raffin',
    'type' : 'dog',
    'owner' : 'kate',
}
pets.append(pet)

pet = {
    'name' : 'rokki',
    'type' : 'dog',
    'owner' : 'nate',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere is what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f" {key} : {value}")
