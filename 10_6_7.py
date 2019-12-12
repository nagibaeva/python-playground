# Addition
print("Enter two numbers and I will add them.")
print("Enter q to exit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You should enter number!")
    else:
        print(f"The answer is {answer}!")