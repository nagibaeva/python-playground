#names = ['ada', 'viki', 'stacy', 'carl', 'admin']
names = []
if names:
    for name in names:
        if name == 'admin':
            print(f"\nHello {name.upper()}, would you like to see todays report?")
        else:
            print(f"\nHello {name.title()}! Thank you for loggin in!")
else:
    print("We need to find some users!")
