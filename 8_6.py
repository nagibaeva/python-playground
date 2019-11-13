# Ex 8_6 City Names
# First option

def city_country(city, country):
    """Display city and country name"""
    print("_______________________________________")
    print(f"{city.title()}, {country.title()}")
    print("_______________________________________")
city_country('bishkek', 'kyrgyzstan')
city_country('moscow', 'russia')
city_country('toronto', 'canada')

# Second option

def city_country_1(city,country):
    """Return formated city and country name"""
    formatted_name = f"'{city.title()}, {country.title()}'"
    return formatted_name
name = city_country_1('bishkek', 'kyrgystan')
print(name)

name = city_country_1('moscow', 'russia')
print(name)

name = city_country_1('toronto', 'canada')
print(name)