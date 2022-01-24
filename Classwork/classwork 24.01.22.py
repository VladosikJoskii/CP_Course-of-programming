'''
# Homework 24.01.22
# Task 1 - NameError Exception

try:
    n1 = 2
    n2 = 3
    print(n3)

except NameError:
    print("Внимание - данной переменной не существует. Напишите ее ниже!")
    n3 = int(input('Введите число: '))
    print(n1 + n2 +n3)

# Task 2 - IndexError Exception

try:
    word = input('Введи слово: ')
    index = int(input('Индекс: '))
    print(word[index])

except IndexError:
    print(f"Ты обращаешься к несуществуюещму элементу\nДлина слова состоит из {len(word)} символов")

# Task 3 - Exception catcher        

try:
    do = ''
    while do != 'exit':
        do = input('Введите любое слово: ')
        num = int(input('Число: '))
        print(do + num)
except TypeError:
    print('Ты пытаешься сложить число и букву')
'''

def send_hi():
    print('Hi user!')

def send_hi_2():
    username = input('Enter username: ')
    print('Hi!', username)

def send_hi_3(name):
    print('Hello,', name)

def time_checker(speed, distance):
    return distance // speed

def shortcut(word):
    d = 'аеёиоыуяюэ'
    for letter in word:
        if letter in d:
            word = word.replace(letter, '')
            print(word)
    return word

print(shortcut('лабрадор-ретривер'))
