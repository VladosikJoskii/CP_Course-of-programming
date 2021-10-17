side = int(input('Введите количество сторон: '))
num = int (input('Введите длинну стороны: '))
if side == 3 :
    print (num * 3)
elif side == 4 :
    print (num * 4)
elif side == 5 :
    print (num * 5)
else:
    print ('К такому меня жизнь не готовила')
