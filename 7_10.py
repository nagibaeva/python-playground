vacations = {}

survey_active = True

while survey_active:
    name = input("\nWhat is your name?: ")
    location = input("\nWhere would you like to go for vacation?: ")

    vacations[name] = location

    repeat = input("\nWould you like to continue? (yes / no): ")
    if repeat == 'no':
        print("\nGood Bye!")
        survey_active = False
print("\n____Results____\n")
for name, location in vacations.items():
    print(f"\t{name.title()} wants to go to {location.title()} for a vacation.")