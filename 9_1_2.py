class Restaurant:
    """Simple Restaurant description."""
    def __init__(self, name, cuisine):
        """Indicating name and cuisine type."""
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        """Describe the name and type of cuisine."""
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine.")
    def open_restaurant(self, time):
        """Indicate the opening hours."""
        print(f"The restaurant {self.name} opens at {time}.")

restaurant_1 = Restaurant('Delli', 'indian')
print(f"\nMy faviorite restaurant is {restaurant_1.name}. Let me tell you more about it.")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant('3 PM')

restaurant_2 = Restaurant('Furusato', 'japanese')
print(f"\nThe other wonderful restaurant is {restaurant_2.name}.")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant('5 PM')

restaurant_3 = Restaurant('Pelmeshki', 'russian')
print(f"\nAlso we have to check {restaurant_3.name}.")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant('1 PM')