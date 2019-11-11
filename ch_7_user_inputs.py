# Chapter 7     User input and While loops

# To recieve information from user use      input()     function.
# Note: this fuction works with terminal and most notepad do not run programs that promts th euser for info.

message = input("\nTell me something, and I will repeat it back to you: ")
print(message.title())

name = input("\nPlease, enter your name: ")
print(f"\nHello, {name.title()}!")

# To create multi-line input strings: assign prompt to a variable then use   input(variable) function:

prompt = "\nIf you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is you last name? "

name_1 = input(prompt)
print(f"\nHello, {name_1.title()} {name.title()}!\n")

# Ex When you ask for information from user using input() function, everything that user inputs is considered as string, so number enetered by user will also be read os string. In order to have inputed information as number use     int() function:

height = input("How tall are you, in inches: ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride a rollercoaster!")
else:
    print('\nYou are not able to ride a rollercoaster.')


# Modulo Operater:
# Modulo operater divides one number by another and returns the reminder:
# 4 % 3 = 1 ; 5 % 2 = 1 ; 23 % 4 = 3
# This opertator is useful to find odd or even number:

number = input("\nEnter a number, and I will tell you if it is odd or even: ")
number = int(number)

if number % 2 == 0:
    print(f"\n\tThe number {number} is even.")
else:
    print(f"\n\tThe number {number} is odd.")