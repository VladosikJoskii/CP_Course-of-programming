from random import randint
list = []
for i in range (randint(1, 10)):
    list.append(randint(1, 10))
for j in list:
    if j == 1:
        result = list.count(j)
print(list)
print(result)