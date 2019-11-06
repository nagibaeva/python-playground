# example of conditional test is    if elif else statements
# Ex: age = 17
#     if age < 8:
#       print("Price is 1 dollar")
#     elif age < 16:
#       print("Price is 3 dollars")
#     else:
#       print("Price is 5 dollars")

# to check for equalty use if == :
# to check for inequality use != :

# 5.8

names = ['jada', 'carry', 'papper', 'admin']
for name in names:
    if name == 'admin':
        print(f"Hello, {name.upper()}, would you like to see report for today?")
    else:
        print(f"Hello, {name.title()}, welcome back!")

print("\nToday is a wonderful day!\n")

# 5.9

print(names)

if names:
    for name in names:
        if name == 'admin':
            print(f"Hello, {name.upper()}, would you like to see report for today?")
        else:
            print(f"Hello, {name.title()}, welcome back!")
else:
    print("Users list is empty.")

del names[:]
print(names)
print("\n\tNow if the list is empty:\n")

if names:
    for name in names:
        if name == 'admin':
            print(f"Hello, {name.upper()}, would you like to see report for today?")
        else:
            print(f"Hello, {name.title()}, welcome back!")
else:
    print("Users list is empty.")
    
# if names:
#     for name in names:
#         if name == 'admin':
#             print(f"Hello, {name.upper()}, would you like to see report for today?")
#         else:
#             print(f"Hello, {name.title()}, welcome back!")
# else:
#     print("Users list is empty.")