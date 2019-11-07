rivers = {
    'nile' : 'egypt',
    'moskva' : 'russia',
    'naryn' : 'kyrgyzstan',
}

for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}.")
print("\n")
for river in rivers.keys():
    print(f"{river.title()} is a very long river!")
print("\n")
for country in rivers.values():
    print(country.title())


# Ex 6 Pooling

best_languages = {
    'sam' : 'python',
    'luke' : 'java',
    'dan' : 'ruby',
    'mary' : 'c',
    'rem' : 'c+',
}

respondents = ['sam', 'luke', 'dan', 'mary', 'rem','liam','naska']

for respondent in respondents:
    if respondent in best_languages.keys():
        print(f"Hi {respondent.title()}, thank you for participating in our servey!")
    else:
        print(f"Hi {respondent.title()}, please fill in our servey.")