def make_sandwich(grain, *ingredients):
    """Display all the ingredients one requested"""
    print(f"\nMaking {grain} sandwich with following inredients:")
    for ingredient in ingredients:
        print(f"-{ingredient}")