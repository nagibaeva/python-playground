# Ex 10_3 Guest

name = input("What is your name?: ")

with open('text_files/guest_name.txt', 'w') as file_object:
    file_object.write(name)