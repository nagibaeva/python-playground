import users

new_admin = users.Admin('cara', 'steels', 19, 'female')
new_admin.describe_user()
new_admin_privileges = [
    'can add post', 
    'can delete post', 
    'can ban user',
    ]
new_admin.privileges.privileges = new_admin_privileges
new_admin.privileges.show_privileges()