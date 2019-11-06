# to make a list use [ ], insert variable into ' '

# to print specific variable from the list specify the order of variable in the list using [ ]. 
# Ex: print(cars[1]) will pring second variable from list cars
# Ex: message = f"My first cars was a {cars[0].title()}."    will print message usinf first variable of the list cars

# to change the variable in the list assign new value using order 
# Ex: cars = ["a", "b", "c"]
#     cars[0] = "o"
#       will change "a" to "o"

# to add additional variable to the list use .append
# Ex: cars.append("o")   will add variable "o" to the list cars
# to add in a  specific order use .insert(order number, "variable")
# Ex: cars.insert(0, "o")   will add variable "o" to the first place

# to remove from the list use del
#Ex: del cars[0]    will remove first variable from the list
# Note: removerd variable will no longer be available
# to remove and then use later try .pop() function
# Ex: removed_cars = cars.pop(0)    will remove first variable from the list cars and make it accesable as removed_cars
# to remove variable from the list also try .remove("variable")

# to make a list in alphabetical order use .sort()
# Note: .sort() will sort order permanently
# use reverse=True to reverse order
# to reorder and keep initial order use .sorted(list name)
# .reverse() will reverse order of the list

# to loop through the list use      for variable in variables:
# Ex:
# cars = ["audi", "bmw", "tesla"]
# for car in cars:
#   print(f"My favorite car is {cars.upper()}!"")
#       will result in printing "My favorite car in audi"   "My favorite car in bmw"   "My favorite car in tesla"

# NUMERICAL LISTS
# for value in range(1, 5):
#   print(value)
#       will end up printing 1 2 3 4

# to print only evens use   range(2, 11, 2)   it will print starting from value and add 2

# to use only part of list use   cars[1:4]      it will use variable starting from 1 to 4
# so you can loop through part of list only using list[start:end]

# to copy a list use [ : ]  which is just as using slice of the list at whole level

# to make a list not accesable to change use tuple by using ()