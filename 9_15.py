from random import choice

#We need to write a loop that will run pulling random items until it matches our ticket number

def get_winning_ticket(possibilities):
    """Return winning ticket from set of possibilities"""
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """Check elemetns of played ticket, if not match of winning ticket, return False"""
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    return True

def make_random_ticket(possibilities):
    """Compose random ticket from set of variables in possibilities"""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket

possibilities = ['1','2','3','4','5','6','7','8','9','10', 'a','b','c','d','f']
winning_ticket = get_winning_ticket(possibilities)
print(f"\n{winning_ticket}")

plays = 0
won = False

max_tries = 1000000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays > max_tries:
        break
if won:
    print("\nWe have winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} attempts to win!")
else:
    print(f"We tried {plays} times without winning!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")