num = int(input('Введите границу числа Фибочи: '))
a = 1
b = 1
i = 0
while i < num - 2:
    c = a + b
    a = b
    b = c
    i = i + 1
print(b)