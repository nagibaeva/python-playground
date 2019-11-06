cars = ['audi', 'toyota', 'subaru','bmw']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())

topping = 'mushrooms'
if topping != "anchovies":
    print('hold the anchovies!')

bike = 'mobi'
if bike != 'mobi':
    print('done')
else:
    print('ok')

answer = 17
if answer != 42:
    print('wrong_answer')

age_0 = 22
age_1 = 18

if age_0 >= 21 or age_1 >= 21:
    print('ok')
else:
    print('wrong')

numbers = ['1', '2', '3']
if '4' in numbers:
    print('yes')
else:
    print('no')

banned_users = ['tuta', 'kati', 'didi']
user = 'tuta'
if user not in banned_users:
    print(f"{user.title()}, you can use the srvice now.")
else:
    print(f"{user.title()}, you can not use the service for 30 days.")