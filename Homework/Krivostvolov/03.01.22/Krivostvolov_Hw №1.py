num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
action = int(input('Что вы хотите сделать?\n1 Добавить\n2 Отнять\n3 Умножить\n4 Поделить\nВвод: '))
if action == 1:
    def add(num_1, numn_2):
        return(num_1 + num_2)
    print(add(num_1, num_2))
elif action == 2:
    def subtraction(num_1, numn_2):
        return(num_1 - num_2)
    print(subtraction(num_1, num_2))
elif action == 3:
    def multiply(num_1, numn_2):
        return(num_1 * num_2)
    print(multiply(num_1, num_2))
elif action == 4:
    def division(num_1, numn_2):
        return(num_1 / num_2)
    print(division(num_1, num_2))
else:
    print('Error')