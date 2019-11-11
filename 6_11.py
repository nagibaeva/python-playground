# Ex 6.11 Cities

cities = {
    'bishkek' : {
        'country' : 'kyrgyzstan',
        'population' : '2 millions',
        'fact' : 'Every winter the polution rate rises up due to the heating season.'
    },
    'oslo' : {
        'country' : 'norway',
        'population' : '700 thousands',
        'fact' : 'The public transportation system is so convinient that most of poplation do not own a car.'
    },
    'newmarket' : {
        'country' : 'canada',
        'population' : '89 thousands',
        'fact' : "You will barely survive without car because public transportation is very poor and the distances are very big."
    },
}
for city, info in cities.items():
    print(f"Here is what I know about {city.title()}:")
    country = f"{info['country']}"
    population = f"{info['population']}"
    fact = f"{info['fact']}"
    
    print(f"\tIt is located in {country.title()}.")
    print(f"\tWith population of {population.title()}.")
    print(f"\t{fact}")