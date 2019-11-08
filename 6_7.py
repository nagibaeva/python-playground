# Ex 7 People

family = {
    'husband' : {
        'first_name': 'rem', 
        'last_name': 'kim', 
        'street': '21 Vantage loop', 
        'city': 'newmarket',
    },
    'son' : {
        'first_name': 'liam', 
        'last_name': 'kim', 
        'street': '21 Vantage loop',
        'city': 'newmarket',
    },
    'mother' : {
        'first_name': 'pana', 
        'last_name': 'amurova', 
        'street': '17 Kozhoyar',
        'city': 'bishkek',
    },
    'father' : {
        'first_name': 'akin',
        'last_name': 'agibaev', 
        'street': '17 Kozhoyar',
        'city': 'bishkek',
    },
}
print("My family list is as follows:")
for relative, personal_info in family.items():
    print(f"\n {relative.title()}")
    full_name = f"{personal_info['first_name']} {personal_info['last_name']}"
    adress = f"{personal_info['street']}, {personal_info['city']}"
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAdress: {adress.title()}")
    
