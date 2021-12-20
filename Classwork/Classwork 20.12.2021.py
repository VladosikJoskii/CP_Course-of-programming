'''
# Hometask 20.12.21
# Task 1 - Login System

login_dict = {'username' : 'User', 'pwd' : 'qwerty123'}

while True:
    pwd = input('Enter a password: ')
    if pwd == login_dict['pwd']:
        print('Success! Welcome!')
        break
    else:
        print('Invalid password!')


# Task 2 - Replacer

data = {'id' : 1, 'name' : 'Bob'}
replacer = {}

keys = list(data.keys())
vals = list(data.values())

for elem in range(len(vals)):
    replacer[vals[elem]] = keys[elem]

print(replacer)

# Task 3 - Number frequency
from random import randint

string_nums = ['zero', 'one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine']
arr = [randint(0,9) for elem in range(randint(2,20))]

res = {}

for elem in range(len(string_nums)):
    res[string_nums[elem]] = arr.count(elem)

print(arr)
print(res)

# Task 4 - Hacking

list_pwd = ['admin', 'test', 'qwerty123', 'qwerty',
            'Admin', 'admin123', 'QWERTY', 'test123',
            'Test123']

login_user = {'id':1, 'name': 'Igor', 'surename' : 'Balkanov', 'pwd' : 'Admin'}

for elem in range(len(list_pwd)):
    if list_pwd[elem] == login_user['pwd']:
        print(f"Password {list_pwd[elem]} is correct!")
        break
    else:
        print(f"Password {list_pwd[elem]} is incorrect!")


# Task 5 - Fruits & Vegetables

fruits = 'apple, banana, orange, lime, lemon'
vegetables = 'cucumber, eggplant, tomato, potato'

word = input('Enter a word: ')

if word in fruits:
    print(f"{word} is a fruit!")
    
elif word in vegetables:
    print(f"{word} is a vegetable")
    
else:
    print('Error!')


# Task 6 - Animal language (snake)

word = input('Enter a word: ')

if 'с' in word:
    word = word.replace("с", "сссс")

print(word)


# Class work 20.12.21

dicts = {'id': {'name':'Igor', 'surename':'Semenov'}}

dicts = list(dicts.values())

res = list(dicts[0].values())
k = list(dicts[0].keys())
print(res + k)


arr = [1,2,3]
tup = (1,2,3)

arr[0] += 5 + tup[0]

print(arr)
print(tup)

print(len(tup))
print(sum(tup))

tup = list(tup)
tup.append(20)

tup = tuple(tup)
print(tup)
'''

# Task - Student exam

exam = int(input('Баллы за экзамен: '))
project = int(input('Кол-во проектов: '))

if exam > 90 or project > 10:
    print('100')

elif exam > 75 and project >= 5:
    print('90')

elif exam > 50 and project >= 2:
    print('75')

else:
    print('Nothing')

# Task - Cylinder Volume

PI = 3.14

radius = int(input('Enter a value: '))
height = int(input('Enter a height: '))

cylinder_volume = round(PI * (radius ** 2) * height, 2)

print('Volume: ', cylinder_volume)
print('Empty volume: ', cylinder_volume // 2)
