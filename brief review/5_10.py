current_users = ['ava', 'david', 'ed', 'sam', 'safron']
new_users = ['liam', 'ilan', 'vane', 'nina', 'ED']

print("The list of current users:")
print(current_users)

print("The list of new users:")
print(new_users)

#not sensetive to upper and lower cases

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, the name {new_user} is already taken. Try something else!\n")
    else:    
        print(f"Hello, {new_user.title()}, welcome to Instagram!\n")
    
#now taking in mind upper and lower cases

new_users_low = []
for new_user in new_users:
    new_users_low.append(f"{new_user.lower()}")

print(new_users_low)

for new_user_low in new_users_low:
    if new_user_low in current_users:
        print(f"Sorry, the name {new_user_low} is already taken. Try something else!\n")
    else:    
        print(f"Hello, {new_user_low.title()}, welcome to Instagram!\n")