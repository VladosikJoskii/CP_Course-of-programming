triangles = int(input('Введите количество треуголников:'))
side_1 = int(input('Введите длинну стороны 1: '))
side_2 = int(input('Введите длинну стороны 2: '))
side_3 = int(input('Введите длинну стороны 3: '))
p_trg = side_1 + side_2 + side_3 
result = p_trg * triangles
print(f"Периметр {triangles} треуголников {result}")