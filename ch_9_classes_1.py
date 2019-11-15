# Classes determine the general behaviour for the whole category of objects.

# Making object from a class called instantiation (konkretiazaciya)

# To create a CLass:
# Ex: Class called Dog, each enstance from the class will store     name and age,   and will have ability to    sit() and roll_over():

# Define a class:   Name:
class Dog:
    # Write a docstring, i.e. comment what this class does.
    """A simple attempt to model a dog."""
# A function that is part of class is a method.
# ___init__ is a default method that Python runs automatically whenever we create a new instance based on our class.
    def __init__(self, name, age):
        # Note that self parameter is always required in the method definition and it comes first of all parameters.
        # self parameter is always passed automatically to instances. We only have to specify other parameters (name and age).
        """Initialize name and age atributes."""
        self.name = name
        self.age = age
        # Any variable that have prefix self is available to every method of class and we will be able to access through any instance created from the class.
        # In other words, any variable with prefix self is available to any further funnction of class (method) and to any instance from class that will be created later.
        # self.name and self.age are called attributes, i.e. accessable through instances.
    def sit(self):
        """Simulate a dog sitting in responce to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response for a command."""
        print(f"{self.name} rolled over.")

# Now lets make an instance representing a specific dog.
# my_dog is instance created from class Dog with atributes name = 'Willie' and age = 6.

my_dog = Dog('Willie', 6)
# After reading this line my_dog = Dog('Willie', 6) Python refers to a method __init__ with atributes 'Willie' and 6 assigned as name and age. 
# To access the atributes of instance use dot notation:     instance_name.atribute (my_dog.name)
print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.\n")

# To call any method defined in class use dot notation:     instance.method()   (my_dog.sit())
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.\n")
your_dog.sit()
your_dog.roll_over()