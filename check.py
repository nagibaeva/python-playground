name = input("Enter you name: ")
age = input("Enter you age: ")
print("Hello, " + name + "! You are " + age)
exit = False
while (not exit):
    print("Whould you like to continue?")
    answer = input("Y/N: ")
    if answer == "Y":
        movie = input("Enter your favorite movie: ")
        music = input("Enter your favorite music style: ")
        print("Hello, " + name + "! You are " + age "Yes")
    if answer == "N":
        exit = True

print("See you later!")