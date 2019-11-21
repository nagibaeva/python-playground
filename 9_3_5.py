class Users:
    """Simple example of users profile."""
    def __init__(self, first_name, last_name, username, age, gender):
        """Indicate a name of a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        """Print full description of user."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"{self.username} is a {self.age} years old {self.gender} with name {full_name.title()}.")
    def greet_user(self):
        """Print personalized greeting."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {full_name.title()}!")
    def show_login_attempts(self):
        """Show the number of attempts."""
        print(f"{self.username} logged in {self.login_attempts} times.")
    def increment_login_attempts(self):
        """Add the given amount of login attempts."""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Reset the number of attempts."""
        self.login_attempts = 0
        print(f"{self.username}'s login number have been resetted.")

yellow_1 = Users('kelly', 'capour', 'kellysuperstar', 28, 'female')
yellow_2 = Users('ryan', 'donnan', 'misterx', 26, 'male')

yellow_1.describe_user()
yellow_1.greet_user()
yellow_1.increment_login_attempts()
yellow_1.increment_login_attempts()
yellow_1.increment_login_attempts()
yellow_1.show_login_attempts()
yellow_1.reset_login_attempts()
yellow_1.show_login_attempts()


yellow_2.describe_user()
yellow_2.greet_user()
yellow_2.increment_login_attempts()
yellow_2.increment_login_attempts()
yellow_2.show_login_attempts()