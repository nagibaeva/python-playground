best_languages = {
    'sam' : ['python', 'c'],
    'luke' : 'go',
    'dan' : ['ruby', 'python'],
    'mary' : 'c++',
    'rem' : ['c+', 'ruby'],
}

# To get list as value for each jey use for command in for command:

for name, languages in best_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")