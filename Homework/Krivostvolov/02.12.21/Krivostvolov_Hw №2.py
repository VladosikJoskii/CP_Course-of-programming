from random import randint
massive = []
for i in range (randint(0, 10)):
    massive.append(randint(0, 10))
for j in massive:
    if j == 1:
        j += 1
        result = massive.count(j)
print(massive)
print(result)