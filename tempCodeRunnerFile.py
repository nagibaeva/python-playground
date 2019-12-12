prompt = "\nWhy do like programming?"
prompt+= "\nEnter q to exit. "

message = ""
while message != 'q':
    message = input(prompt)
    if message != 'q':
        print(f"{message} is a good reason!")
        with open('text_files/answers.txt', 'a') as f:
            f.write(f"{message}\n")
    else:
        print("\nGood bye!")  