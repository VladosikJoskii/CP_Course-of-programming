students = int(input('Введите количество учащихся: '))
num = 1
for i in range(0, students, 1):
    mark = int(input(f"Введите оценку ученика {num}: "))
    num += 1
    mark += mark
middle = mark // students
print(f"Средняя оценка учеников : {middle}")