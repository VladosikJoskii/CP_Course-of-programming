students = int(input('Введите количество учащихся: '))
num = 1
result_mark = 0
for i in range(0, students, 1):
    mark = int(input(f"Введите оценку ученика {num}: "))
    num += 1
    result_mark += mark
middle = result_mark / students
print(f"Средняя оценка учеников : {middle}")