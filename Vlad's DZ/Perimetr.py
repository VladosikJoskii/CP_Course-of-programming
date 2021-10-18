s=int(input('Длина одной из сторон '))
d=input('Какая фигура? ')
if d=='Треугольник':
    print(s*3)
elif d=='Квадрат':
    print(s*4)
elif d=='Пятиугольник':
    print (s*5)
else :
    print('Error')
