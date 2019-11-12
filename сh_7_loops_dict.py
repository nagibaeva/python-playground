# While loops with Lists:

# Moving items from list to list

# Example: newly regustered users but not verified yet. After verifiction how to move them to the list of verified users?

# Start with users thet need to be verified, and empty list of verified users:

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
# pop function removes one variable from the back of the list

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display all confirmed users

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Note that we did not used     for loop    because, when using   for loop  we cannot modify the list used. So instead we used   while loop, which is running until the list is empty.
print('\n')
# Now, in order to remove one repeating variable from the list we use   while loop and remove() function:

pets = ['dog', 'cat', 'dog', 'cat', 'bird', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

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
    repeat = input("\nWhould you let another person respond? (yes\no): ")
    if repeat == 'no':
        polling_active = False
        print("Thank you and good bye!")
    
    # Polling is colmplete. SHow the results.

    print("\n---Poll Results---")
    for name, response in responses.items():
        print(f"{name} would like to climb: {response}.")