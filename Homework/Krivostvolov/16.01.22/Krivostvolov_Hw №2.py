print ('Login: Alex')
print ('Password = 3425hgbu678')
chance = 3
correct_login = 'Alex'
correct_password = '3425hgbu678'
user_login = input ('Введите свой логин: ')
user_password = input ('Введите пароль: ')
if chance > 0:
    if user_login != correct_login:
        for i in range (chance):
            chance -= 1
            user_login = input ('Вы ввели неправильный логин. Введите свой логин ещё раз: ')
    elif correct_password != user_password:
        for i in range (chance):
            chance -= 1
            user_password = input ('Вы ввели неправильный пароль. Введите свой парольыва ещё раз: ')
    else:
        print('Добро пожаловать!')
else:
    print('Error')