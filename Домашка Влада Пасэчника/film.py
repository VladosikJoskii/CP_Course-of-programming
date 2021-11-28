film=input('Фильм:')
st=int(input("Рейтинг= "))
while st != 10:
    st += 1
    print("Рейтинг вырос",st)
    if st==10:
        print("Шик")
        break
print(film,"рейтинг :" ,st)
