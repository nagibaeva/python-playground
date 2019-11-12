# Ex Deli   lists

sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'teriyaki', 'pastrami']
finished_sandwiches = []

print("\nWe run out of pastrami sandwiches. Sorry! Choose something else.\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    if current_sandwich != 'pastrami':
        print(f"I am making you {current_sandwich} sandwich!")
        finished_sandwiches.append(current_sandwich)
    else:
        print(f"Sorry, we run out of {current_sandwich}. Please choose something else.")

while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')

print("\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} sandwich")

