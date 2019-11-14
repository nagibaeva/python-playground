# Ex 8_12 Sandwiches

def make_sandwich(grain, *ingredients):
    """Display all the ingredients one requested"""
    print(f"\nMaking {grain} sandwich with following inredients:")
    for ingredient in ingredients:
        print(f"-{ingredient}")
make_sandwich('white', 'chicken', 'pickles', 'ketchup')
make_sandwich('grey', 'ham', 'tomato', 'mozzarella')
make_sandwich('white', 'turkey', 'pepper', 'cheddar')

# Ex 8_13 User profile

def build_profile(first, last, age, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['age'] = age
    return user_info
user_profile = build_profile(last = 'agibaeva', first = 'nazgul', age = 29, education = 'economics', university = 'uio')

print(f"\n{user_profile}")

# Ex 8_14 Cars

def building_car(brand, model, **additional_info):
    """Build a dictionary with all known information about car"""
    additional_info['brand'] = brand
    additional_info['model'] = model
    return additional_info
car = building_car(model = 'crv', brand = 'honda', color = 'green', year = 1999)

print(f"\nMy first car was: {car}.")