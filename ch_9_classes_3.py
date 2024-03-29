# Inheritance:  when you write specialized class based on already existing class.
# Original class - parent class
# New class - child class
# New class can inherit from parent class all atributes and methods, but it is free to define new attributes and methods on its own.

# Ex: write class ElectricalCar on the basis of Car class.

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

my_new_car = Car('honda', 'crv', '2018')
print(my_new_car.get_descriptive_name())

# Note: the parent class should be part of current file and should go first (since order matters).
# To make child class use:      __init__ function     
# and in order to call methods from parent class use:       super().__init__(attributes)   function.
# Note you can add any attributes and methods to the child class.

class Battery:
    """Model a battery from electric cars."""
    def __init__(self, battery_size=75): #Note that battery_size is optional parameter if no value is provided.
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go to about {range} miles on a full charge.")

class ElectricCar(Car):
    """Respresent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# If the parent class contains methods that does not fit the child class, you can override this particular method.
# To override any method from parent class in child class:      define a method in child class with the same name as the method in parent class that you want to override. In this case, python will ignore the method in parent class and use the new in child class.

# Ex. The electric car does not have gas tank, so we can override given method:

    # def fill_gas_tank(self):
    #     """Electric cars don't have gast tank."""
    #     print("This car doesn't need a gas tank!")

# You can use classes as attributes to classes, i.e. classes in classes.
# Above: We will update class ElectricCar with class Battery. (First create class Battery, then use it as attribute in class ElectricCar). In class Battery we will store every method assosiated with battery of the car. Then we assign the class Battery as attribute of class ElectricCar. And now we can access every method in class Battery using:   instance.class_set_as_attribute.method()