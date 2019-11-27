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

class Battery:
    """Model a battery from electric cars."""
    def __init__(self, battery_size=75):
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
    def upgrade_battery(self):
        """Check and upgrade battery size"""
        if self.battery_size < 100:
            print(f"\nUpgrading the battery size.")
            self.battery_size = 100
        else:
            print("\nThe battery size is upgraded!")

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
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()