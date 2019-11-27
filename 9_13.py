from random import randint
class Die:
    """Attempt to imitate simple dice roll"""
    def __init__(self, sides=6):
        """Itinialize attributes of dice"""
        self.sides = sides
    def roll_die(self):
        """Imitate random dice roll"""
        return randint(1, self.sides)
dice_6 = Die()

results= []
for roll in range(10):
    result = dice_6.roll_die()
    results.append(result)
print(results)

dice_10 = Die(sides=10)

results= []
for roll in range(10):
    result = dice_10.roll_die()
    results.append(result)
print(results)

dice_20 = Die(sides=20)

results = []
for roll in range(10):
    result = dice_20.roll_die()
    results.append(result)
print(results)