class Restaurant:
    """Simple Restaurant description."""
    def __init__(self, name, cuisine):
        """Indicating name and cuisine type."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the name and type of cuisine."""
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self, time):
        """Indicate the opening hours."""
        print(f"The restaurant {self.name} opens at {time}.")
    
    def customers_served(self):
        """Show number of customers served."""
        print(f"{self.name} served {self.number_served} customers so far.")
    
    def update_customers(self, customers):
        """
        Set number of customers to a given value.
        Reject the change if number is lower."""
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("You cannot put less customers than it already have!")
    
    def increment_customers(self, clients):
        """Add the given amount of clients to the cusmoters number."""
        self.number_served += clients

restaurant_1 = Restaurant('Torro', 'american')

print(f"\nMy faviorite restaurant is {restaurant_1.name}. Let me tell you more about it.")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant('3 PM')

restaurant_1.customers_served()
# First option
restaurant_1.number_served = 100
restaurant_1.customers_served()
# Second option
restaurant_1.update_customers(250)
restaurant_1.customers_served()

restaurant_1.update_customers(150)
restaurant_1.customers_served()
#Third option
restaurant_1.increment_customers(390)
restaurant_1.customers_served()

