# age = 1
# age = 3
# age = 11
# age = 17
# age = 25
age = 66

if age <2:
    category = "a baby"
elif age <4:
    category = "a toddler"
elif age <13:
    category = "a kid"
elif age <20:
    category = "a teenager"
elif age <65:
    category = "an adult"
else:
    category = "an elder"
print(f"You are {category}!")
