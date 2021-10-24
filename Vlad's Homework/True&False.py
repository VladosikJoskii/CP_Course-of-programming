print('Вы будете считать чи не являеться число1 меньше числа2 ')
a=int(input("Ведите число 1 "))
b=int(input("Ведите число2 "))
c=(a<b)
if c==True:
    print('Yes!')
else:
    print("No!")

# Best Practice
# Refactored version

a=int(input("Введите число 1: "))
b=int(input("Введите число 2: "))

if a < b:
    print('Yes')
else:
    print('No')
