from random import randint

series = ['p1','2','3','4','5','6','7','8','9','10', 'a','b','c','d','f']

lottery_ticket = []

for roll in range(4):
    ticket_variable = series[randint(0,len(series))]
    lottery_ticket.append(ticket_variable)
print("\nThe winning ticket number is:")
print(lottery_ticket)
