prompt = "\nWhat is your name?:"
prompt+= "\nEnter q for exit. "

name = ""
while name != 'q':
    name = input(prompt)
    if name != 'q':
        print(f"\nHello, {name.title()}!")
        with open('text_files/guest_book.txt', 'a') as f:
            f.write(f"{name.title()}\n")
    else:
        print("\nGood bye!")