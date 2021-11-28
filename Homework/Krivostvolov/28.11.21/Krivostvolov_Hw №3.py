from random import randint
num = 0
film_name = 'film'
stop_num = 0
print('Для прекращения поиска нажмиет 1, для продолжения нажмите любое другое число')
while stop_num != 1:
    film_rate = randint (0, 100)
    num += 1
    print(f"Название фильма: {film_name} {num} \nРейтинг фильма: {film_rate}")
    stop_num = int(input('Ваше действие: '))
else:
    print('0_0')