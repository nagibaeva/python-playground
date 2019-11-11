# Ex 6.10 Favorite Numbers

favorite_numbers = {
    'tonya' : [17, 98, 54],
    'lera' : [16, 55, 38],
    'bema' : [1, 7, 9],
    'naska' : [21, 88, 7],
    'rem' : [16, 24, 10],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()} likes the following numbers: ")
    for number in numbers:
        print(f"\t{number}")