prompt = "What is your name?: "
prompt+= "\nEnter q to exit. "

name = ''
while True:
    name = input(prompt)
    if name != 'q':
        print(f"Welcome, {name.title()}!\n")
        answer = input("Why do you study python?: ")
        with open('text_files/new_name_answer.txt', 'a') as f_o:
            f_o.write(f"{name.title()}\n")
            f_o.write(f"{answer.title()}\n")
        repeat = input("Whould you like to continue? (y/n) ")
        if repeat == 'n':
            print("Thank you for answering!")         
            break
    else:
        print("\nGood Bye!")
        break