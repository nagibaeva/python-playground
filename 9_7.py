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
        

class Admin(Users):
    """Simple description of admin"""
    def __init__(self, first_name, last_name, age, gender, username='admin'):
        """Attributes of parent class"""
        super().__init__(first_name, last_name, username, age, gender,)
        self.privileges = []
    def show_privileges(self):
        print(f"\nAs an administrator {self.username} have the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")

yellow_1 = Users('kelly', 'capour', 'kellysuperstar', 28, 'female')
yellow_2 = Users('ryan', 'donnan', 'misterx', 26, 'male')
yellow_3 = Admin('ada', 'jhons', 25, 'female')
yellow_3.privileges = ['can add post', 'can delete post', 'can ban user']

yellow_3.describe_user()
yellow_3.greet_user()
yellow_3.show_privileges()