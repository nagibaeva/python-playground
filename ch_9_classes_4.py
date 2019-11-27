# Importing a single class

# Lets created separate modul with class Car from previous example and name it car.py
# Now import the class Car from module car.py

from car import Car

my_new_car = Car('honda', 'crv', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Storing multiple classes in a Modul 
# one modul can store as many classes as you need, only they have to be related somehow. 
# In order to import one particular class from a modul containing several classes:

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing multiple classes from one modul: list requested classes using     ,     
# from name_of_the_modul import name_of_the_class_1, name_of_the_class_2

from car import Car, ElectricCar

volkswagen = Car('volkswagen', 'passat', 2019)
print(volkswagen.get_descriptive_name())

tesla_2 = ElectricCar('tesla', 'roadster', 2019)
print(tesla_2.get_descriptive_name())

# Importing entire module
# import module
# variable = module_name.Class_name(parameters)

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_roadster = car.ElectricCar('tesla', 'rodaster', 2019)
print(my_roadster.get_descriptive_name())

# Python standard library
from random import randint
randint(1,6)