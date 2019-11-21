# You can modify attributes of instance directly or write methods that update attributes in specific ways.

class Car:
    """A simple attemt to summarize a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print statement showing cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """
        Set odometer reading to a certain value
        Reject the change if it attemts to roll the odometer back
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

# Above is standard class and instance from class Car.
# Now lets modify it and add mileage of car.
# There are three ways to modify instance: 
#   1) change the value directly through an instance;
#   2) set a value through a method;
#   3) increment a value through a method (add a certain value to it).

# Option 1:     change the value directly through an instance:

# Assign new value to attribute associated with given instance directly:
#           instance.attribute = value
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Option 2:     set a value through a method i.e. write a method that updated the value of attribute:
# Add new method that updates milage:
#   def update_odometer(self, milage):
        # """Set odometer reading to a certain value"""
        # self.odometer_reading = milage
# assign the value of milages in ():  instance.attribute(value)

my_new_car.update_odometer(35)
my_new_car.read_odometer()

my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_new_car.update_odometer(40)
my_new_car.read_odometer()

my_new_car.update_odometer(36)
my_new_car.read_odometer()

# We made this method little bit more complicated with if sentence, which checks if the assigned value is not bigger that existing value.

# Option 3: increment a value through a method (add a certain value to it).
# Sometimes you want to add certain amount to current value of attributes instead of assigning completely new value.

# add new method to the class Car:      
# def increment_odometer(self, miles) 
# self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)
print(f"\n{my_used_car.get_descriptive_name()}")

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()