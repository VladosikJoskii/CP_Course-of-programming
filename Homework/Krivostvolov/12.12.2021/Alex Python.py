from random import randint
numbers = []
massives = []
ones = 0
for i in range (randint(1, 5)):
    numbers.append(randint(0, 10))*5
massives.extend(numbers)
print (massives)