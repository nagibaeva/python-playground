# Passing a list

# Define function as plural, so python will expect working with list. (greet_userS)
# Define plural parameter. (nameS)

def greet_users(names):
    """Display a greeting message for each user in a list"""
# Write code working with lists:    
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)

# Define a list and assign function with specific argument, i.e. defined list. Argument = list 'usernames'.
usernames = ['hannah', 'sam', 'alice']
greet_users(usernames)


# Modyfing list.
# We can modify list without assigning function:

# First option
# Start with design that needed to be printed:
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until non are left
#Move each design to completed_models after printing

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#Display all completed models:
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Second option
# Modify list using functions:

# We will construct two functions: first will print designs, second will summarize the prints:

print("\n")

# Define function with two parameters:

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until non are left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

#Define funtion with one parameter:

def show_completed_models(completed_models):
    """ Display all completed models """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)