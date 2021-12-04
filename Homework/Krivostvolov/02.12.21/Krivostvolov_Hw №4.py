from random import randint
print ('Нажите на 1 что-бы закончть программу, на любое другое число для продолжения')
massive = []
start = 0
while start != 1:
    s_1 = randint (1, 20) * randint (1, 20)
    s_2 = randint (1, 20) * randint (1, 20)
    print(s_1)
    print(s_2)
    if s_1 > s_2:
        massive.append('Поместился')
    else:
        massive.append('Не поместился')
    print(massive)
    start = int(input('Ваше действие: '))
else:
    print ('')