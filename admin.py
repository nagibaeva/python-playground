from user import Users

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