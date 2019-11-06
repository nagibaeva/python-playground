current_users = ['ada', 'viki', 'stacy', 'carl', 'admin']

current_users_up = []
for current_user in current_users:
    current_users_up.append(f'{current_user.upper()}')
print(current_users_up)

new_users = ['ADA', 'ronin', 'carl', 'pete', 'dave']

for new_user in new_users:
    if new_user in current_users:
        print(f"\nSorry, the name {new_user} is taken.")
    elif new_user in current_users_up:
        print(f"\nSorry, the name {new_user} is taken.")
    else:
        print(f"\nCongratilations! The name {new_user} is available!")
