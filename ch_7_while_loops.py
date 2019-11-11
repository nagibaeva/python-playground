# While loop will run program until condition to stop is true:

current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

# You can engage user to stop the while loop.

prompt = "\nTell me somthing and I will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message.title())

# In order to remove last quit print, use if statement: i.e. print if other than quit

prompt = "\nTell me somthing and I will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"\n{message.title()}")
    else:
        print("\nGood bye!")

# When there are many conditions to stop the program, it it better to use one condition to check if it is true then run the program, i.e. use   flag method.

prompt = "\nTell me somthing and I will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program: "

# lets mark our flag as active: 

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
        print("\nGood Night!")
    else:
        print(f"\n {message.title()}")

# To exit while loop immediately, without any other code use:   break statement:

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' if you want to exit.) "

# While True will run forever unless it reaches a break statement.

while True:
    city = input(prompt)

# break will end program without any further condition
    if city == 'quit':
        print("\nBye!")
        break
    else:
        print(f"\nI'd love to visit {city.title()}")

# To return to thebeggining without breaking the loop use   continue:

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)