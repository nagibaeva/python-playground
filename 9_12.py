from user import Users
from admin import Admin, Privileges

third_admin = Admin('rem', 'kim', 26, 'male')
third_admin.describe_user()

third_admin_privileges = [
    'can control the feed',
    'can accept new users',
    'can delete and ban users',
]
third_admin.privileges.privileges = third_admin_privileges

third_admin.privileges.show_privileges()