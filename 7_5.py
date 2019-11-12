age = input("Enter your age: ")
age = int(age)

if age < 3:
    print("\nPrice for your ticket is: 0.")
elif age < 12:
    print("\nPrice for your ticket is: 10 dollars.")
else:
    print("\nPrice for your ticket is: 15 dollars.")