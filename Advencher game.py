end='Игра Окончена'
print('Ты просто смелый путешественик и есть у тебя 3 пути')
print("1--В лес")
print("2--В пустыню")
print("3--В океан")
askk=int(input('Куда ты пойдёш? '))
#Лес
if askk==1:
    print("Вы пошли в лес")
    print("В скоре вы заблудились но в далеке вы видите какой то дом")
    if askk==1:
        print("Вы подошли к дому")
        print("У вас 3 варианта")
        print('1--Зайти в дом')
        print('2--Не заходить в дом и обследовать месность')
        print('3--Уйти проч')
        ask=int(input('Что будете делать? '))
        if ask==1:
            print("Вы зашли в дом, дверь скрипела но вы не обратили внимания")
            print("У вас 2 варианта")
            print("1--Осмотреть")
            print("2--Уйти")
            ask=int(input('И так, твой вариант? '))
            if ask==1:
                print("Вы осмотрели дом и видите подвал и дверь куда то")
                print("1--Подвал")
                print("2--В дверь")
                ask=int(input('Куда пойдешь? '))
            else:
                print(end)
                if ask==1:
                    print("Вы спустились подвал и увидели огромных крыс мутантов")
                    print("Вы попытались убежать но вас сьели")
                    print(end)
                elif ask==2:
                    print("Вы увидели ведьму и потом вас очаровали чары её и жили долго и щаслево")
                    print("Плохая концовка")
        elif ask==2:
            print("Вы решили осмотреть месность и сзади дома был огромный сад вы поняли что вы тут не одни")
            print("У вас 2 варианта")
            print("1--Быстро побежать к дому")
            print("2--Подойти к саду и поесть")
            print("3--Убежать проч")
            ask=int(input('Что будете делать? '))
            if ask==1:
                print("Вы быстро бежиите из зо всех сил к дому но вы чуствуете слабость")
                print("1--стараться")
                print("Тебе не куда бежать хи хи хи хи")
                print(end)
            elif ask==2:
                print("Вы подошли и взяли первый попавшийся плод но укусивши его вы взлетели но потом разбились")
                print(end)
            elif ask==3:
                print("Бежавши вы выбижали из леса и попали в райский город")
                print("Он прекрасен")
                print(" Вы получили хорошое настроение и концовку")
            else:
                print("lol")
    elif ask==3:
        print("Вы ушли проч и вас сьели волки")
        print(end)
    else:
        print("Ква ква квауаауааyааyаaaa")
# Пустиня   
if askk==2:
    print("После многих миражей вы видите структуру похожую на храм")
    print("У вас 3 варианта")
    print("1--Побежать к храму")
    print("2--Пойти к храму")
    print("3--Спокойно умереть")
    ask=int(input('Твой выбор? '))
    if ask==1:
        print("Вы застряли в зыбучих песках")
        print(end)
    elif ask==2:
        print("Вы подошли к храму и внутри бы разрушеный колодец посмотревши туда вы видите воду")
        print("Вы имеете 2 варианта")
        print("1--Осмотреть")
        print("2--Попробывать достать влягой")
        print("???")
        ask=int(input('Выбирай! '))
        if ask==1:
            print("Вы осматривали храм и вдруг попали в ловушку")
            print("У вас есть 3 варианта")
            print("1--Посмотреть в рюдзак")
            print("2--попробывать разгрысть")
            print("3--сильно ворочиться и кричать")
            ask=int(input('Что же ты выбирешь? '))
            if ask==1:
                print("Вы открыли рюдзак")
                print(" и видите целых 4 прдмета")
                print("1--разкладной нож")
                print("2--фляга")
                print("3--немного не доеденой еды")
                print("4--немного одежды")
                ask=int(input('Какой предмет ты выбирешь? '))
                if ask==1:
                    print("Вы взяли нож и разрезали верёвку")
                    print("После этого вы убежали из храма ")
                    print("Куда побежишь ")
                    print("1--прямо")
                    print("2--направо")
                    print("3--на лево")
                    ask=int(input('Куда собрался? '))
                elif ask==2:
                    print("Вы пытались бить верёвку флягой но в пустую ")
                    print(end)
                elif ask==3:
                    print("Вы взяли еду и уронили кусочек напол")
                    print("Потом вы заметили мышь которая сьела этот кусочек")
                    print("Вы намазали верёвку едой и верёвку сьели мыши но потом сьели вас")
                    print(end)
                elif ask==4:
                    print("Вы достали одежду но поняли что это безполезно")
                    print(end)
            elif ask==2:
                print("Вы попытались разгрысть сеть но онабыла очень прочная")
                print(end)
            elif ask==3:
                print("Вы сильно ворочились и кричали и на ваши крики прибежала мумия")
                print("Осталось всего то 3 варианта ")
                print("1--попробывать махать через сетку что бы ударить  мумию")
                print("2--договориться с ней")
                print("3--погибнуть")
                ask=int(input('Что ты выбирешь? '))
        elif ask==2:
            print("Вы пытались достать воду но случайно упали туда")
            print("Какой у вас план")
            print("1--пытаться залазить по камням")
            print("2--напиться")
            print("3--окончить игру")
            ask=int(input('Что ты выбирешь? '))
        elif ask==333:
            print("Новый персонаж открыт")
            print("Steve")
            print("Хотите сыграть за него?")
            print("1--Steve")
            print("2--Путешественик")
            ask=int(input('Продолжить за.. '))
            if ask==1:
                print("Ты стал кубическим")
                print("И перед тобой появился портал")
                print("Зайти в него?")
                print("1--Да")
                print("2--Нет")
                ask=int(input('Ну так что будешь делать? '))
                if ask==1:
                    print("Ты зашол в портал и оказался в майнкрафте")
                    print("Вы когда то играли в эту игру и поэтому вы быстро развились")
                    print(" и вот первая ноч выживания")
                    print("1--Поспать")
                    print("2--Воевать")
                    ask=int(input('Ваш вариант? '))
                elif ask==2:
                    print("ТттТыыы ссс лл000ммалл иииииггггрррр  у оато")
                    print("Error 404")
                else:
                    print(end)
            elif ask==2:
                print("Ну и зачем ты сюда пришёл?")
                print(end)
    elif ask==3:
        print("Вы пересохли")
        print(end)
    else:
        print(end)
#Океан
if askk==3:
    print("Вы сделали лодку и поплыли в океан")
    print("Впереди появился туман")
    print("Из-за тумана вы ничего не видите,но слышите много разних звуков")
    print("У вас 3 варианта")
    print('1--Поплыть с закрытыми глазами')
    print('2--Стоять на месте')
    print('3--утонуть')
    ask=int(input('Что будете делать? '))
    if ask==1:
        print("Вы закрыли глаза и продолжили плыть но ваша лодка страно покачивалась")
        print("У вас есть 3 варианта")
        print("1--открыть глаза")
        print("2--продолжить плыть")
        print("3--Закричать")
        ask=int(input('Делай свой выбор? '))
        if ask==1:
            print("Вы решили открыть глаза и видите огромное чудище!")
            print("Выбор")
            print("1--погладить")
            print("2--напасть")
            print("3--обойти")
            if ask==1:
                print("Вы смогли погладить чудище и оно помахало вам и уплыло ")
                print("")
                print("")
                print("")
                print("")
            ask=int(input('Выбор за тобой '))
        elif ask==2:
            print("Вы простояли на месте 10 минут, но тут вас накрыло водой и вы оказались в желудке кита ну как бы не пытался ваши кулаки, меч вы умерли")
            print(end)
        elif ask==3:
            print("На ваш крик приплыли русалки и очеравали своей красотой. Ну и естествено сьели")
            print(end)
    elif ask==2:
        print("Вы стояли на месте и почуствывали воду под ногами и О БОЖЕ МОЙ ЛОДКА ТОНЕТ")
        print("Ваши действия:")
        print("1--Покинуть судно")
        print("2--Как-то выгрибать воду")
        ask=int(input('Что будете делать?!! '))
        if ask==1:
            print("Вы покинули судно и только потом вспомнили что в океане есть акулы")
            print(end)
        elif ask==2:
            print("Вы начали выгрибать воду и видите саму дырку и заделавыете её")
            print("Вы сильно утомились поэтому у тебя есть 3 варианта")
            print("1--поспать")
            print("2--продолжить плыть")
            print("3--утопиться")
            ask=int(input('Что будешь делать? '))
            if ask==1:
                print("Вы уснули но когда вы проснулись вы поняли что вы на острове")
                print("Варианта всего три")
                print("1--Развести лагерь")
                print("2--Обследовать остров")
                print("3--Улудшить лодку и жить в ней")
                ask=int(input('Что же будем делать док? '))
            elif ask==2:
                print("Вы так сильно хотели спать что даже не заметили остров,Вы заплыли в какуюта пещеру а потом уснули")
                print("Проснувшись вы обдумываете действия ")
                print("1--Остаться тут жить")
                print("2--починить лодку и уплыть за приключениями")
                print("3--достать свой меч и закричать")
                ask=int(input('Какой вариант выберешь? '))
            elif ask==3:
                print("Вы утонули и дальше...")
                print(end)
    else:
        print("Пацан к успеху шол но не доплыл")  

