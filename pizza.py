def make_pizzaa(size, *toppings):
    """Summarize pizza we are about to make"""
    print(f"\nMaking pizza size -{size} inch with following toppings:")
    for topping in toppings:
        print(f"- {topping}")