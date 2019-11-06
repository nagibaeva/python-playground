# ex 5.1

superheroes = ['hulk', 'iron man', 'thor', 'capitan america', 'widow']

for superhero in superheroes:
    if superhero == 'thor':
        print (superhero.upper() + " is amaizing!")
    else:
        print(superhero.title() + " is OK.")

for superhero in superheroes:
    if superhero in superheroes == "thor":
        print("\ncatch")
    else:
        print("\nmissed")

        exit = False
        while(not exit):
            command = input("DO you want to exit? (yes/no)")
            if command == 'yes':
                exit = True
            
        print("Bye bye")