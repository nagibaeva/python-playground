# Ex 7.1 Rental Car

car = input("\nEnter what kind of car would you like to try: ")
print(f"Let me see if I can find you a {car.title()}.")

# Ex 7_2 Restaurant seating

seats = input("How many people are attending the dinner?: ")
seats = int(seats)

if seats > 8:
    print("Please wait for a bigger table.")
else:
    print("Table is ready.")

# Ex 7_3 Multiple of ten

number = input("\nEnter any number and I will tell you if it is multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is multiple of 10.")
else:
    print(f"\nThe number{number} is not multiple of 10.")