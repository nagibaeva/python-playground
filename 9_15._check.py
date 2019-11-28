from random import choice

def get_winning_ticket(series):
    """Form a winning ticket"""
    winning_ticket = []

    while len(winning_ticket) < 5:
        pulled_item = choice(series)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """Check if played ticket is winning ticket"""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

def make_played_ticked(series):
    """Make random ticket"""
    ticket = []

    while len(ticket) < 5:
        pulled_item = choice(series)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket

series = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 'a', 'b', 'c', 'd', 'e', 'f', 'g']

winning_ticket = get_winning_ticket(series)
print(winning_ticket)

played = 0
won = False

max_tries = 1000

while not won:
    new_ticket = make_played_ticked(series)
    won = check_ticket(new_ticket, winning_ticket)
    played += 1

    if played > max_tries:
        break
if won:
    print("You won!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"Number of tries is {played}")
else:
    print("You lost!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"Number of tries: {played}")

