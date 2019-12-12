# Exceptions are special objects that manage the errors that arise during the code running.
# Simple, you tell python what to do when the error arises, and if the error arises, python will manage error and run code further.

# Use   try-except blocks   to manage errors:

# ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

print("Give me two numbers, and I will divide them.")
print("Enter q to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nEnter second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!")
    else:
        print(answer)
# Without try except else block this example will show error. 
# 1) We shifted the operation itself in a try block, 
# 2) The code that depends on operation code is moved to esle block, 
# 3) And the Error case solution is shown in except block.

# So the Rule pf try-except-else blocks is as follows:
# 1) Python attempts to run the code in try block. (There should be code that might cause an exception to be raised)
# 2) The except block tells python what to do if the exception arises.
# 3) And when you need some code to be implemented after the successful attempt of try block, it should go to else block. (i.e. what you wnat to do if the code is successfully past)

# FileNotFoundError

filename = 'text_files/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    #Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"\nThe file {filename} has about {num_words} words.")