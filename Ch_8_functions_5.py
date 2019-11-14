# Sometimes you don't know how many arguments will be required, so in this case you can make arbitrary number of arguments for one parameter. To do so, use    def function(*parameter):

def make_pizza(*toppings):
    """Print the list of toppings requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('cream cheese', 'olives', 'pepper')

#Now lets make more complicated:

def make_pizza_1(*toppings):
    """Summarie pizza we are about to make"""
    print("\nMaking pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza_1('pepperoni')
make_pizza_1('cream cheese', 'olives', 'pepper')

# Positional and Arbitrary Arguments:

# When you want to use positional and arbitrary arguments: make sure that corresponding parameter for arbitrary agrument stands last while defining function:

def make_pizza_2(size, *toppings):
    """Summarize pizza we are about to make"""
    print(f"\nMaking pizza size -{size} inch with following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza_2(16, 'pepperoni')
make_pizza_2(18, 'mushrooms', 'extra cheese', 'chicken')

# Arbitrary Keyword Arguments

# Sometimes you want to use number of arguments but don't know what information will be passed to the function.
# In this case use dictionary of arbitrary arguments    **parameter:

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'enstein', location = 'princeton', field = 'physics')
# Note: parameters location and field were not indicated in definition of function, but since we created open dictionary **user_info it will accept all not indicated parameters with arguments.

print(f"\n{user_profile}")

# Modules. Importing from modules.

# Module is a file .py containing code you want to import into program.

# Importing Entire Module
# To import entire module (i.e. all the code contained in module) use:

# import name_of_module
# name_of_module.function(parameters)

import pizza

pizza.make_pizzaa(16, 'pepperoni')
pizza.make_pizzaa(18, 'onion', 'chicken', 'extra cheese')

# Importing Specific Functions
# To import only specific functions use: 
# from module_name import function_name (Note: you can import as many functions as you want by separating them by , )

from pizza import make_pizzaa

make_pizzaa(18, '4 cheese')
make_pizzaa(24, 'salad', 'ananas', 'ham')

# Importing using AS to Give a Function Alias
# Use it in case if importing function may conradict with any function in the program:
# from module_name import function_name as fn    where fn is any alternative name for imported function
# fn(parameters)

from pizza import make_pizzaa as mp 

mp(12, 'ham')
mp(14, 'vegetables', 'cheese')

# Importing using AS to give a module an alias
# import module_name as mn

import pizza as p

p.make_pizzaa(30, 'cheese')
p.make_pizzaa(28, 'chicken', 'mashroom')