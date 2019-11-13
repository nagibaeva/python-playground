# Using a Function with While loops:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formated"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me you name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        print("\nGood Bye!")
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        print("\nGood Bye!")
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}!")