print ('Приветствуем Вас в игре Knightn The Dragonborn!\nВашей задачей будет спасти принцессу из лап древнего дракона')
start = int(input ('Нажмите "Start" что-бы начать игру...\n1 Start\n2 Nope\nВвод:'))
if start == 1:
    print ('\nНачинаем игру. Внимание! Если у Вашего персонажа не останется здоровья до конца игры, то Вы проиграете и прийдётся начинать всё заново!')
    print ('\nИ так, Ваши приключения начинаются!\nС утра по раньше, гуляя по рынку, Вы наткнулись на объявление где было написано, что дракон выкрал принцессу и за ёё спасение положена награда: Гора золота, а также рука и серде принцессы. И так как у Вас пожизненная ипотека, Вам приглянулся этот квест. Забежавши к себе домой Вы на скорую руку берёте свой меч, который достался Вам от отца, а ему от его отца, а он подобрал его за кузней. Первое что Вы видите, вышедши из города, это куча монстров, которых нужно победить и тем самым повысить свои навыки для победы над драконом ')
    print ('\nВаша характеристика:')
    pl_lvl = 1
    pl_hp = 100
    pl_dmg = 30
    player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
    print (player)
    print('\nПервый монстр которого Вы встретили был великий и ужасныый Римуру Темпест, он обладал сильнейшей магией и мог с лёгкстю переломать Вам кости')
    print ('\nИнформация:\nСила врага - невообразима\nПри победе ваш уровень повыситься на максимальный\nНо если это обычная слизь, то ёё атака: 10, здоровье: 30\nВаши навыки повысятся на 1 Lvl.')
    challenge_1 = int(input('\nВаши действия:\n1 Напасть\n2 Убежать\nВвод:'))
    enemy_dmg = 10
    if challenge_1 == 1:
        pl_lvl += 1
        pl_hp -= enemy_dmg
        pl_dmg += 10
        player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
        print ('\nВы победили !')
        print (player)
        print('\nХмммммм.... похоже это быда обыкновенная слизь')
    else:
        print('\nВы в ужасе убежали от этой слизи')
    print('\nПосле событий с первым монстром Вы продолжили свои похождения. Идя по протоптоной тропе Вы увидили высокое дерево в дупле которого, совершенно случайно, оказались две большие спящии летучие мыши, которые по ночам терроризировали жителей из Вашего города.')
    print('\nИнформация:\nСила врага: 30\nЗдоровье врага: 40\nПри победе ваш уровень повыситься на 2 Lvl.')
    challenge_2 = int(input('\nЧто Вы собираетесь с ними сделать ?\n1 Напасть\n2 Не трогать и пойти себе дальше\nВвод:'))
    enemy_dmg = 30
    if challenge_2 == 1:
        pl_lvl += 2
        pl_hp -= enemy_dmg
        pl_dmg += 20
        player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
        print ('\nВы победили !')
        print (player)
        print ('\nХоть это и были летучии мыши, но они больно кусались')
    else:
        print('\nВы решили их не трогать, ведь когда Вы спасёте принцессу, то зачем Вам вовращатся в свой горд ')
    print('\nИдя далее Вы вспоминаете, что неподолёку находится небольшая деревня, а это значит, что Вы сможете там отдохнуть и переночивать. Взбираясь на небольшой холм,что-бы осмотрется, Вы видите ту самую деревню, но буквально в 100 метрах от неё шла какая-то битва. Ёё участниками были - люди из деревни, а также 3 орка-великана. Вы задумались: "Если я помогу деревлянам, то они могут меня за это вознаградить. НО также я могу попасть под удар этого орка-великана и мне будет не сладко"')
    print('\nИнформация:\n Если Вы поможете этим людям, то в будущем - это Вам сильно поможет. Но если у Вас низкий уровень, то можете погибнуть')
    challenge_3 =int(input('\nВаши действия:\n1 Помочь\n2 Подождать пока они сами справятся\nВвод:'))
    choise_1 = 0
    if challenge_3 == 1 and pl_lvl < 2 and choise_1 ==0:# ничего нового 2 2 1 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print('\nУ вас низкий уровень навыков, Вы ничем не сможете помочь тем защитникам')
        print('\nДождавшись пока атака орков-великанов будет отбита Вы решили всё таки зайти в эту деревню. Самое главное сейчас было найти место для отдыха. Распросивши у местных жителей Вы узнали, что можете переночивать в конюшне, но только одну ночь. Выспавшись и востановивши силы Вы вновь подались в путь')
        pl_hp = 100
    elif challenge_3 == 2 and choise_1 ==0:# ничего нового 1 1 2
        print('\nДождавшись пока атака орков-великанов будет отбита Вы решили всё таки зайти в эту деревню. Самое главное сейчас было найти место для отдыха. Распросивши у местных жителей Вы узнали, что можете переночивать в конюшне, но только одну ночь. Выспавшись и востановивши силы Вы вновь подались в путь')
        pl_hp = 100
    elif challenge_3 == 1 and pl_lvl >=2:
        print('\nВы на всех порах побежали на помощь и крича на орков разные обидные слова "Хорошо, что поблизости небыло детей", тем самым переманив внимание обидчеков на себя. Этим моментом воспользывались защитники деревни, окруживши они заманили их в ловушку. Ну а Вы разогнавшись прыгнули со скалы...Кхм. То есть споткнувшись упали между двумя великанами. К счастью для Вас, жители уже были готовы для финального удара, все всместе убили их. И тут, облегчённо взохнувши Вы не заметили как одна из тушек падает прямо на Вас')
        pl_lvl += 1
        pl_hp = '???'
        pl_dmg += 10
        player = 'Hp:'+(str(pl_hp))
        print('\n' + str(player))
        print('\nВы проснулись в одинокой комнате. У Вас болело всё тело и Вы ничего не помнили. Внезапно Вы услышали стук в дверь и к Вам в комнату вошёл какой-то мужчина, он Вам когото напоминал.\nМужчина: Здравствуй нежданный гость! Я один из тех, кто оборонял эту деревню в тот день и меня зовут Рэйнхард. Ну как оклемался после вчерашнего ? Тебе повзло, что ты упал на мягкую почву и тебя не раздовила великаном, а только впечатало в землю. Ладно перейду к главному, судя по внешнему виду ты обычный горожанин, который решил спасти принцессу. Ты уж прости, но когда мы тебя сюда несли, то у тебя из карамана выпал этот листок в котором всё было сказано. Так вот, за твою помощь я готов дать тебе доспехи среднего качества, а также могу привести в порядок твой меч, как ты с таким затупившимся мечём сюда вообще добрался ? Либо попросить кого-нибудь из своей команды помочь в этом нелёгком деле')
        choise_1 = int(input('\nТак что ты выбираешь?\n1 Взять доспехи "+50 к максимальному запасу здоровья и +50 к силе"\n2 Попросить кого-нибудь в помошники "Меньше получаемого урона, а также рост силы"\nВвод:'))
    if choise_1 == 1: # новая броня 1 1 1 1 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        pl_hp = 200
        pl_dmg += 50
        player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
        print('\nХорошо, когда будешь отправлятся в путь, зайди ко мне и я тебе всё выдам.')
        print('\nОтдохнувши и прийдя в себя, Вы нашли того мужчину и по договору получили свою награду, сразу после этого Вы вышди из этой деревни и продолжили свой путь')
        print('\n'+ str(player))
        print('\nВыйдя из города и пройдя уже несколько километров, Вы наткнулись на дикого кабана, но выглядил он как-то особо устрашающе.')
        print('\nИнформация: Сила врага:100, здоровье:115\nПри победе: +2 lvl.')
        challenge_4 = int(input('\n1 Напасть\n2 Попытаться обойти\nВвод:'))
        enemy_hp = 115
        enemy_dmg = 100
        if challenge_4 == 1:
            pl_hp = pl_hp - enemy_dmg
            pl_lvl += 2
            pl_dmg += 20
            player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
            print('\nПобеда')
            print(player)
            print('\nНу и боровы нынче пошли, Вы ели управились')
        else:
            print('\nРешив его обойти, Вы начили делать небольшой крюк, но какбан всё равно Вас почуял и атаковал. Рванув со всег ног Вам всё-таки удалось от него удрать, но он Вас сильно измотал')
            pl_hp -=20
            player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
            print(player)
        print('\nИзбавившись от кабана Вы продолжили свой путь. Дальше Ваш путь лежал через местность где справа от Вас находились возвышености и скалы, а с левой стороны лес, где по слухам могли обитать матёрые волки. Идя по тропе, Вы встретили по пути пастушку, которая переводила своё стадо овец. Это было очень рекдое событие, когда пасти овец доверяли девушкам, к тому-же в таких далёких и опасных от церкви местах.\nПастушка: Приветствую странник, меня зовут Нора Арендт, а это мой верный друг и пощник - пёс Энек. Если Вы собираетесь продолжить свой путь через эту местность, то спешу Вас огорчить. В последнее время тут участились атаки волков на людей, поэтому могу предложить свои услуги и сопроводить Вас до ближайшего города Рубинхайгена. Ну как согласны ?')
        print('\nКогда вы уже почти прошли эту местность, то на выходе на вас напали стая волков. Их было пятеро, но кажется это были не те, про которых были рассказы.')
        print('\nИнформация: Сила противника: 150, здоровье: 120 при победе: +2 lvl или +4 lvl, если всех перебить')

    elif choise_1 == 2: # похождение с напарником 1 1 1 2 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     print('\nХоршо, я познакомлю Вас, но чуть позже, а сейчас отдыхай')
     print('\nЧерез два дня этот мужчина снова пришёл к Вам, но с ним был кто-то ещё.\nРэйнхард: Знакомся, это твой напарник\nНапарник:Приветствую, меня прозвали "Тенью", в благодарность за Вашу помощь нашей деревни я вызвалась помочь Вам в ваших похождениях')
     print('\nТень была одета в мантию охотника из-за которой было выдно только часть лица, а также она обладала, как ни странно, охотничьим луком')
     print('\n После знакомства Вы собрали некоторые свои вещи и вместе со своим напарником отправились в путь')
     pl_hp = 100
     pl_dmg = 70
     friend_1_dmg = 50
     friend_1_hp = 100
     friend_1_lvl = 5
     print('\nХарактрестика Тени: Hp:' + str(friend_1_hp) + ' Dammage:' + str(friend_1_dmg) + ' Level '+ str(friend_1_lvl))
     print('\nВаша характеристика: Hp:' + str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Level '+ str(pl_lvl))
     print('\nВыйдя из города и пройдя уже несколько километров, вы наткнулись на дикого кабана, но Тень, как опытный охотник, подсказала Вам что это очень опытный и опасный враг. Если на него охотится в одиночку, то получить тяжёлые - неизбежно, но так как нас двое, шансы на успех велики')
     print('\nИнформация: Сила врага: 100, здоровье: 115\nПри победе: +1 lvl.')
     challenge_4 = int(input('\nВаши действия:\n1 Напасть\n2 Попытаться обойти\nВвод:'))
     enemy_hp = 115
     enemy_dmg = 100
     if challenge_4 == 1:
         pl_hp = pl_hp - (enemy_dmg // 2)
         pl_lvl += 1
         pl_dmg += 10
         friend_1_lvl += 1
         friend_1_dmg += 10
         player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
         friend_1 ='Hp:'+(str(friend_1_hp) + ' Dammage:' + str(friend_1_dmg) + ' Lelvel:' + str(friend_1_lvl))
         print('\nПобеда')
         print('Ваша характеристика: '+ str(player))
         print('Характеристика Тени: ' + str(friend_1))
         print('\nТень была права, только вы начили приближься к нему, как он сразу учуял и напал на вас, даже если-бы Вы решили его обойти, вряд-ли это вышло')
         print('\nИзбавившись от кабана вы продолжили свой путь. Дальше ваш путь лежал через местность где справа от вас находились возвышености и скалы, а с левой стороны лес, где по слухам могли обитать матёрые волки. Идя по тропе, вы встретили по пути пастушку, которая переводила своё стадо овец. Это было очень рекдое событие, когда пасти овец доверяли девушкам, к тому-же в таких далёких и опасных от церкви местах. После того как вы немного пообщались с ней, разошлись каждый своей дорогой. Через какое-то время Тень рассказала Вам историю которую она слышала:\n"Судя по слухам ёё зовут Нора Арендт и из-за того, что она проводит овец через опасные места теряя при этом максимум 2-3 овцы, когда обычно теряют половину стада, церковь думает, что она одержима демоном и хочет чтобы она сгинула в одном из этих мест, но как на зло, она всё время выживает. Я не хотела спрашивать действительно ли это она, ведь вдруг правда что она одержима"\nОт этих слов Вам стало не по себе, но вы продолжили путь.')
         print('\nКогда вы уже почти прошли эту местность, то на выходе на вас напали стая волков. Их было пятеро, но кажется это были не те, про которых были рассказы.')
         print('\nИнформация: Сила противника: 150, здоровье: 120 при победе: +2 lvl или +4 lvl, если всех перебить')
     else:
        print('\nРешив его обойти, вы начили делать небольшой крюк, но какбан всё равно вас почуял и атаковал. Рванув со всег ног вам всё-таки удалось от него удрать, но он вас сильно измотал')
        pl_hp -= 20
        friend_1_hp -= 20
        player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
        friend_1 = 'Hp:'+(str(friend_1_hp) + ' Dammage:' + str(friend_1_dmg) + ' Lelvel:' + str(friend_1_lvl))
        print('\nВаша характеристика: '+ str(player))
        print('Характеристика Тени: ' + str(friend_1))
        print('\nИзбавившись от кабана вы продолжили свой путь. Дальше ваш путь лежал через местность где справа от вас находились возвышености и скалы, а с левой стороны лес, где по слухам могли обитать матёрые волки. Идя по тропе, вы встретили по пути пастушку, которая переводила своё стадо овец. Это было очень рекдое событие, когда пасти овец доверяли девушкам, к тому-же в таких далёких и опасных от церкви местах. После того как вы немного пообщались с ней, разошлись каждый своей дорогой. Через какое-то время Тень рассказала Вам историю которую она слышала:\n"Судя по слухам ёё зовут Нора Арендт и из-за того, что она проводит овец через опасные места теряя при этом максимум 2-3 овцы, когда обычно теряют половину стада, церковь думает, что она одержима демоном и хочет чтобы она сгинула в одном из этих мест, но как на зло, она всё время выживает. Я не хотела спрашивать действительно ли это она, ведь вдруг правда что она одержима"\nОт этих слов Вам стало не по себе, но вы продолжили путь.')
        print('\nКогда вы уже почти прошли эту местность, то на выходе на вас напали стая волков. Их было пятеро, но кажется это были не те, про которых были рассказы.')
        print('\nИнформация: Сила противника: 150, здоровье: 120 при победе: +2 lvl или +4 lvl, если всех перебить')
    challenge_5 = int(input('\nМожно попытаться обойтись малой кровь, а именно: разбить их строй и добежать до стен уже виднеещегося замка, где вам поможет стража. Или попытаться всех перебить\n1 Добраться до стражи\n2 Перебить их\nВвод:'))
    enemy_hp = 24*5
    enemy_dmg = 30*5
    if challenge_5 == 1:
        pl_hp = pl_hp - (enemy_dmg //4)
        pl_lvl += 2
        pl_dmg += 20
        friend_1_lvl += 2
        friend_1_dmg += 20
        friend_1_hp = friend_1_hp - (enemy_dmg//2)
        player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
        friend_1 ='Hp:'+(str(friend_1_hp) + ' Dammage:' + str(friend_1_dmg) + ' Lelvel:' + str(friend_1_lvl))
        print('\nПобеда')
        print('Ваша характеристика: ' + str(player))
        print('Характеристика Тени: ' + str(friend_1))
        print('\nПоблагодаривши стражников за помощь вы направилсь в город, под названием Рубинхайгем. В нём можно было восстановить силы и переночивать, а также расспросить у местного населения насчёт дракона. Войдя в сам город вы сразу направились в постоялый двор для аренды комнаты. Идя по улице вы заметли, что идёт набор в добровольци на убийство дракона. Такого обьявление нельзя было игнорировать и вы сразу направились на общий збор крторый вот-вот должен был начаться. Прийдя на него вы удивились, что людей оказалось слишком мало, точнее только один человек. Как только он вас увидел, сразу направился в вашу сторону.\nНезнакомец:Приветствую! Я Урцуг Шварц или же меня прозвали "Щитоносцем". Слава господу, что кто-то откликнулся на моё обьявление, обычно в это время люди готовятся к ярмарке, которая будет через 5 дней. Как я вижу у тебя уже есть напарник, но позволь и мне вступить в твой отряд. Я хочу лишь отомстить этому дракону за то, что спалил мою деревню до тла.')
        choise_2 = int(input('\n1Взять Щитоносца в напарники (Щитоносец будет принимать основной удар на себя)\n2И сами справимся\nВвод:'))
        if choise_2 == 1:
            print('\nЩитоносец: Огромное Вам спасибо! Если вы не успели снять комнату в постоялом дворе, то могу пригласить в покои моей гильдии, всё равно до завтрашнего дня там никого не будет')
            friend_2_hp = 500
            friend_2_dmg = 60
            friend_2_lvl = 9
            friend_2 ='Hp:'+(str(friend_2_hp) + ' Dammage:' + str(friend_2_dmg) + ' Lelvel:' + str(friend_2_lvl))
            print('Характеристика Щитоносца: ' + str(friend_2))
        else:
            print('Очень жаль.... Чтож, тогда прийдётся ждать моих согильдийцев, а вам могу пожелать лишь удачи')
    else:
        pl_hp = pl_hp - (enemy_dmg //2)
        pl_lvl += 4
        pl_dmg += 40
        friend_1_lvl += 4
        friend_1_dmg += 40
        friend_1_hp = friend_1_hp - (enemy_dmg//2)
        player = 'Hp:'+(str(pl_hp) + ' Dammage:' + str(pl_dmg) + ' Lelvel:' + str(pl_lvl))
        friend_1 ='Hp:'+(str(friend_1_hp) + ' Dammage:' + str(friend_1_dmg) + ' Lelvel:' + str(friend_1_lvl))
        print('\nПобеда')
        print('Ваша характеристика: ' + str(player))
        print('Характеристика Тени: ' + str(friend_1))
        print('\nС трудом справившись с волками вы, под удивлённый взгляд стражи, ввошли в город под названием Рубинхайгем. В нём можно было восстановить силы и переночивать, а также расспросить у местного населения насчёт дракона. Войдя в сам город вы сразу направились в постоялый двор для аренды комнаты. Идя по улице вы заметли, что идёт набор в добровольци на убийство дракона. Такого обьявление нельзя было игнорировать и вы сразу направились на общий збор крторый вот-вот должен был начаться. Прийдя на него вы удивились, что людей оказалось слишком мало, точнее только один человек. Как только он вас увидел, сразу направился в вашу сторону.\nНезнакомец:Приветствую! Я Урцуг Шварц или же меня прозвали "Щитоносцем". Слава господу, что кто-то откликнулся на моё обьявление, обычно в это время люди готовятся к ярмарке, которая будет через 5 дней. Как я вижу у тебя уже есть напарник, но позволь и мне вступить в твой отряд. Я хочу лишь отомстить этому дракону за то, что спалил мою деревню до тла.')
        choise_2 = int(input('\n1 Взять Щитоносца в напарники (Щитоносец будет принимать основной удар на себя)\n2 И сами справимся\nВвод:'))
        if choise_2 == 1:
            print('\nЩитоносец: Огромное Вам спасибо! Если вы не успели снять комнату в постоялом дворе, то могу пригласить в покои моей гильдии, всё равно до завтрашнего дня там никого не будет')
            friend_2_hp = 500
            friend_2_dmg = 60
            friend_2_lvl = 9
            friend_2 ='Hp:'+(str(friend_2_hp) + ' Dammage:' + str(friend_2_dmg) + ' Lelvel:' + str(friend_2_lvl))
            print('Характеристика Щитоносца: ' + str(friend_2))
        else:
            print('Очень жаль.... Чтож, тогда прийдётся ждать моих согильдийцев, а вам могу пожелать лишь удачи')
    pl_hp = 100
    friend_1_hp = 100
    print('Переночивавши в покоях, Вы и ваша команда снарядились на "Финальный рывок". Выйдя из города вам предстояло поднятся на гору, где обитал этот дракон. Пройдя несколько километров, вы наконец добрались до этой горы, осталось лишь взабратся на самую вершину. Работая в команде вы наконец добрались до нужного вам места и увидели его - Огромного и страшного дракона, а также небольшую щель откуда доносились чьи-то крики. Недолго думая Вы вступили в бой с драконом.')
    final = int(input('\nВы готовы ?\n1 ДА, ЗА ПЕЧЕНЬКИ!\n2 Нет\nВвод:'))
    team_hp = pl_hp + friend_1_hp + friend_2_hp
    team_dmg = pl_dmg + friend_1_dmg + friend_2_dmg
    boss_hp = 1000
    boss_dmg = 120
    y_result = boss_hp - team_dmg
    b_result = team_hp - boss_dmg
    if final == 2:
        print('\nГоблина ответ! В АТАКУ!')
        print('\nFinal fight\nХарактеристика дракона: HP: 1000 Dammage: 100 Level: ???')
        print('\nВаш ход!')
        print('\n' + str(boss_hp) + ' - ' + str(team_dmg))
        print(y_result)
        print('Ход дракона!')
        print('\n' + str(team_hp) + ' - ' + str(boss_dmg))
        print(b_result)
        print('\nВаш ход!')
        print('\n' + str(y_result) + ' - ' + str(team_dmg))
        y_result -= team_dmg
        print(y_result)
        print('Ход дракона!')
        print('\n' + str(b_result) + ' - ' + str(boss_dmg))
        b_result -= boss_dmg
        print(b_result)
        print('\nВаш ход!')
        print('\n' + str(y_result) + ' - ' + str(team_dmg))
        y_result -= team_dmg
        print(y_result)
        print('Ход дракона!')
        print('\n' + str(b_result) + ' - ' + str(boss_dmg))
        b_result -= boss_dmg
        print(b_result)
        print('\nВаш ход!')
        print('\n' + str(y_result) + ' - ' + str(team_dmg))
        y_result -= team_dmg
        print(y_result)
    else:
        print('Воистину за печеньки !')
        print('\nFinal fight\nХарактеристика дракона: HP: 1000 Dammage: 100 Level: ???')
        print('\nВаш ход!')
        print('\n' + str(boss_hp) + ' - ' + str(team_dmg))
        print(y_result)
        print('Ход дракона!')
        print('\n' + str(team_hp) + ' - ' + str(boss_dmg))
        print(b_result)
        print('\nВаш ход!')
        print('\n' + str(y_result) + ' - ' + str(team_dmg))
        y_result -= team_dmg
        print(y_result)
        print('Ход дракона!')
        print('\n' + str(b_result) + ' - ' + str(boss_dmg))
        b_result -= boss_dmg
        print(b_result)
        print('\nВаш ход!')
        print('\n' + str(y_result) + ' - ' + str(team_dmg))
        y_result -= team_dmg
        print(y_result)
        print('Ход дракона!')
        print('\n' + str(b_result) + ' - ' + str(boss_dmg))
        b_result -= boss_dmg
        print(b_result)
        print('\nВаш ход!')
        print('\n' + str(y_result) + ' - ' + str(team_dmg))
        y_result -= team_dmg
        print(y_result)
elif start == 2:
    print('Baka')
