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

class IcecreamStand(Restaurant):
    """Represent aspect of restaurant, specific to Icecream specialied"""
    def __init__(self, name, cuisine='ice_cream'):
        """Initialize attributes of parent class"""
        super().__init__(name, cuisine)
        self.flavors = []
    
    def show_flavor(self):
        """Show what flavor are available"""
        print(f"\nFollowing flavors are avaiable:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

fresco = IcecreamStand('fresco')
fresco.flavors = ['vannila', 'choco', 'berry']

fresco.describe_restaurant()
fresco.show_flavor()