# FUNCTIONS
# Functions are named blocks of code to do one specific job. So, within the code in order to write same code to do one type of job, you can call a function, that will do the code.

# Ex: fuction that prints a greeting:

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# To define a function use:     def name_of_function(what kind of info the function needs to do the job)     module.
# Remember simplier:    def function():

#           def greet_user():

# Next goes body of the function: 
# 1) docstring, which describes what function does:

#           """Display a simple greeting."""
# Remember to enclose in triple quotes:     """Docstring"""

# 2) actual code, i.e. what function has to do:

#           print("Hello!")

# Next, is when you want to use the fuction, you call it. 
# To call a function: write the name of the function.


# To pass info to a function insert information into () of def module:  def function(info):
# and specify info while calling fucntion:

def greet_user_1(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}! How are you?")

greet_user_1('anna')
greet_user_1('king ali')

# In the preceding function: 
#           username is     a parameter 
#           'anna' is       an argument

# Parameter is piece of information that function needs to do it's job
# Argument is piece of information that is passed from a function call to function.

# Functions can have multiple parameters, so they require multiple arguments.
# Agruments can be passed to fucntions in different ways: 
#   1) Using Positional arguments (where arguments need to be in the same order as parameters)
#   2) Using Keyword arguments (where each argument consist of variable name and a value)
#   3) Using Lists and Disctionaries

# Positional Arguments: Order matters.

def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

describe_pet('dog', 'willie')

# Note: First argument 'hamster' is assigned to first parameter animal_type, and second argument 'harry' assigned to second parameter pet_name. So, order matters.

# Keyword Arguments: is a name-value pair that you pass to a function.

def describe_pet_1(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet_1(animal_type = 'hamster', pet_name = 'harry')

# Note: Keyword arguments implies that you specify parameter and its argument in function call. Be sure to use exact name of parameters as in function's defenition.

# Default values (in parameters)
# You may set a default value and python will automatically reffer to default parameter if not specified in the call.

def describe_pet_2(pet_name, animal_type = 'dog'):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet_2(pet_name = 'willie')

# Note: same output would give following call: describe_pet_2('willie')
# Note: describe_pet_2(animal_type = 'hamster', pet_name = 'harry') will ignore default value 'dog' since function's call specified argument for parameter animal_type.

# Note: You may combine: positional agruments, keyword arguments and default values.