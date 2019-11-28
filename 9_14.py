from random import randint

series = ['p1','2','3','4','5','6','7','8','9','10', 'a','b','c','d','f']

lottery_ticket = []

for roll in range(4):
    ticket_variable = series[randint(0,len(series))]
    lottery_ticket.append(ticket_variable)
print("\nThe winning ticket number is:")
print(lottery_ticket)

#The answer by author: 

from random import choice

series = ['1','2','3','4','5','6','7','8','9','10', 'a','b','c','d','f']

winning_ticket = []

while len(winning_ticket) < 4:
    pulled_item = choice(series)
    if pulled_item not in winning_ticket:
        print(f"We pulled {pulled_item}!")
        winning_ticket.append(pulled_item)
print("\nThe winning ticket is:")
print(winning_ticket)
