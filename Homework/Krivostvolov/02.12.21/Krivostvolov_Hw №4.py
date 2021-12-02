from random import randint
input('Нажите на 1 что-бы закончть программу, на любое другое число для продолжения')
list = []
start = 0
while start != 1:
    a_1 = randint (1, 20)
    b_1 = randint (1, 20)
    a_2 = randint (1, 20)
    b_2 = randint (1, 20)
    s_1 = a_1 * b_1
    s_2 = a_2 * b_2
    print(s_1)
    print(s_2)
    if s_1 > s_2:
        list.append('Поместился')
    else:
        list.append('Не поместился')
    print(list)
    start = int(input('Ваше действие: '))
else:
    print ('')