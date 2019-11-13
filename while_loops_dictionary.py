# Now lets see how to store the user input in a dictionary (user name and user input)

responses = {}

# Set a flag to indicate that polling is active

polling_active = True

while polling_active:
    # Ask for users name and input
    name = input("\nWhat is your name?: ")
    response = input("Which mountain you would like to climb one day?: ")

    # STore response in the dictionary
    responses[name] = response

    # Find out if to continue 
    repeat = input("\nWhould you let another person respond? (yes \\ no): ")
    if repeat == 'no':
        print("Thank you and good bye!")
        polling_active = False
    
# Polling is colmplete. SHow the results.

print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb: {response.title()}.")