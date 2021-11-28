from random import randint
stop_num = 0
print('Для прекращения поиска нажмиет 1, для продолжения нажмите любое другое число')
while stop_num != 1:
    film_name = input('Введите название филма: ')
    film_rate = randint (0, 100)
    print(f"Название фильма: {film_name} \nРейтинг фильма: {film_rate}")
    stop_num = int(input('Ваше действие: '))
else:
    print('0_0')