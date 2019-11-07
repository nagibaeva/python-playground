# Looping through dictionaries

# Looping through all key-value pairs
# To loop through key-value pairs use   dictionary.items()  method:

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\nNow lets consider next example:\n")

best_languages = {
    'sam' : 'python',
    'luke' : 'java',
    'dan' : 'ruby',
    'mary' : 'c',
    'rem' : 'c+',
}

for name, language in best_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Note In the second example the variables key and value are named name and language. (Remember, first goes key then comma, and then value)

# Looping through keys in dictionary
# To loop through keys in dictionary use:   dictionary.keys()   method:

print("\n")

for name in best_languages.keys():
       print(name.title())
# Note: same code would work as: 
# for key in best_languages:
#        print(key.title())

friends = ['dan', 'sam']

print("\n")
for name in best_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = best_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}!")

# To check if particular key in dictionary use:     if variable_name in dictionary.keys():  method:

if 'rem' in best_languages.keys():
    print(f"How do you liked our pool, {name.title()}?")
if 'rem' not in best_languages.keys():
    print("Rem, please take our pool!")

# To loop a dictionary in particular order use:     sorted(dictionary.keys()):  method:

print("\n")
for name in sorted(best_languages.keys()):
    language = best_languages[name].title()
    print(f"{name.title()}, thank you for taking the pool! Now we know your favorite language is {language.title()}!")

# Looping through values:
# To loop through values use:   dictionary.values()     method:

best_languages['naska'] = 'python'
print("\nThe following languages have been mentioned in the pool:")
for language in best_languages.values():
    print(language.title())

# To exclude repeated keys or values in dictionary use:     set(dictionary.values())    method:
print("\nExcluding repeated languages, the following list remains:")
for language in set(best_languages.values()):
    print(language.title())