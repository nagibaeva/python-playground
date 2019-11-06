# Three age groups: younger than 4 - free; age 4-18 - 25$; age 18-above - 40$.
# print message about fees.

age = 3
if age <4:
    print('Your entry cost is $0')
elif age <18:
    print('Your entry cost is $25')
else:
    print('Your entry cost is $40')

# different method to do the same thing

age = 30
if age <4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40
print(f"Your ticket price is ${price}.")