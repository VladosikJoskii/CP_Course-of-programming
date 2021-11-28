triangles = int(input('Введите количество треуголников:'))
num = 0
result_p_trg = 0
for i in range (0, triangles):
    side_1 = int(input('Введите длинну стороны 1: '))
    side_2 = int(input('Введите длинну стороны 2: '))
    side_3 = int(input('Введите длинну стороны 3: '))
    p_trg = side_1 + side_2 + side_3
    num += 1
    print(f"Периметр трекгольника {num} равен: {p_trg}")
    result_p_trg += p_trg
result = p_trg * triangles
print(f"Периметр {triangles} треуголников {result}")