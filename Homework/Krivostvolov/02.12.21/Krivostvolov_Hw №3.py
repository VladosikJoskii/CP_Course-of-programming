import math
median_massive = []
figures = int(input('Введите количество треуголников: '))
for i in range(figures):
    side_a = int(input('Введите сторону 1: '))
    side_b = int(input('Введите сторону 2: '))
    side_c = int(input('Введите сторону 3: '))
    if side_a != '' and side_b != '' and side_c != '':
        median = round (math.sqrt((2 * side_a**2 + 2 * side_b**2 - side_c**2)//2), 1)
        median_massive.append(median)
        median_massive.sort()
        print(median)
    else:
        print('Убедитесь, что Вы написали все 3 стороны треугольника')
print(median_massive)