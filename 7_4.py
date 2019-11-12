#first method using flag
prompt = "\nWhat topping do you want to add:"
prompt += "\nEnter 'quit' to finish request. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print("\nToppings are chosed. Your pizza is preparing!")
    else:
        print(f"\nYour toppings will include: {message.title()}")

# Second opting using break method
prompt = "\nWhat topping do you want to add:"
prompt += "\nEnter 'quit' to finish request. "

while True:
    message = input(prompt)

    if message == 'quit':
        print("\nToppings are chosed. Your pizza is preparing!")
        break
    else:
        print(f"\nYour toppings will include: {message.title()}")

# Third method using conditional test

prompt = "\nWhat topping do you want to add:"
prompt += "\nEnter 'quit' to finish request. "

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"\nYour toppings will include: {message.title()}")
    else:
        print("\nToppings are chosed. Your pizza is preparing!")