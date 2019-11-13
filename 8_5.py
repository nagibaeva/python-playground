# Ex 8_5 Cities

def describe_city(city, country = 'kyrgyzstan'):
    """Display information about city"""
    print(f"{city.title()} is in {country.title()}.")
describe_city('bishkek')
describe_city('moscow', 'russia')
describe_city('oslo', country = 'norway')