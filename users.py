"""Module to describe users and admin"""

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

class Privileges:
    """Simple descriptions of privileges of admin"""
    def __init__(self, privileges=[]):
        """Initialize the attributes"""
        self.privileges = privileges
    def show_privileges(self):
        """Print statement showing the privileges"""
        print("\nAdmin has the following privileges:")
        for privilege in self.privileges:
            print(f"-{privilege.title()}")        

class Admin(Users):
    """Simple description of admin"""
    def __init__(self, first_name, last_name, age, gender, username='admin'):
        """Attributes of parent class"""
        super().__init__(first_name, last_name, username, age, gender,)
        self.privileges = Privileges()