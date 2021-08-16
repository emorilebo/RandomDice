# import random
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())
from pathlib import Path


path = Path()
for file in path.glob('*.py'):
    print(file)

#path = Path("ecommerce1")

#print(path.exists())
#print(path.mkdir())
#print(path.rmdir())