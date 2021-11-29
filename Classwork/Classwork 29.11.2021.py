'''
# Task 1 - Triangles

perimeter = 0

count_triangle = int(input('Введи кол-во треугольников: '))

for triangle in range(count_triangle):
    side_1 = int(input('Сторона 1: '))
    side_2 = int(input('Сторона 2: '))
    side_3 = int(input('Сторона 3: '))
    perimeter += side_1 + side_2 + side_3

print(f"Периметр всех треугольников: {perimeter}")

# Task 2 - Students
students = int(input('Введите кол-во студентов: '))
marks = 0

for mark in range(students):
    marks += int(input("Оценка студента: "))

print(f"Средняя оценка: {round(marks / students, 2)}")

# Task 3 - Films
from random import randint

film = ''
stop = '1'
while 1:
    if film == stop:
        break
    
    else:
        film = input('Введи название фильма: ')
        print(film + '|' + str(randint(1,10)))

# Task 4 - Flash

file = 0
f1 = 256
f2 = 512
f3 = 1024
f4 = 2097152 # 2 TB

while f2 > 50:
    file += 1
    f2 -= 50

print('512MB' + '|' + str(file))


#...
    
# Статические ТД. Особенности

string = 'Dog'

print(string)
print(string.replace('g', 'c'))
print(string)

'''

# Списки (Lists/Arrays)
from random import randint
arr = []

for elem in range(randint(3,10)):
    arr.append(randint(1,5)) # append добавляет в конец списка элемент

arr.sort() # сортирует значения в порядке возрастания

for ones in arr:
    if ones == 1:
        arr.append('Found 1')
        
       
print(arr)

arr.pop(2)
print(arr)


