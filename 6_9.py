# Ex 6.9 Favorites Places

favorite_places = {
    'rem' : ['home', 'lcbo', 'cinematica'],
    'naska' : ['parents home', 'home', 'book shoop'],
    'liam' : ['home', 'daycare', 'toys store'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")