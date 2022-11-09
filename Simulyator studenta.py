# Короче, симулятор студента
# идеи: купить препода, сделать случайные события(вы получили
# автомат, у вас день рождения, выгорание), команда назад
# сука похмелье не так работает

import random

red = '\033[31m'
yellow = '\033[33m'
green = '\033[32m'
blue = '\033[36m'
navy = '\033[34m'
purple = '\033[35m'
grey = '\033[37m'
black = '\033[30m'
clear = '\033[0m'


def Luck(value):
    a1 = random.randint(1, value)
    a2 = random.randint(1, value)
    if a1 == a2:
        return True

    return False


def Inp(v, ifnot, quest):
    ans = input(MakeGray(quest))
    while ans != str(v) and ans != str(v - 1) and ans != str(v - 2) and ans != str(v - 3) and ans != str(v - 4):
        print(ifnot)
        ans = input(MakeGray(quest))
    xyu = int(ans)
    return xyu


def Balance(v, perso):
    ecol = green
    scol = green
    kcol = green
    dcol = green
    if perso == '1':
        dmax = 15
    elif perso == '2' or perso == '4':
        dmax = 20
    elif perso == '5':
        dmax = 40
    else:
        dmax = 30

    if e < 10:
        ecol = yellow
        if e < 0:
            ecol = red
    if s < 10:
        scol = yellow
        if s < 0:
            scol = red
    if k < 10:
        kcol = yellow
        if k < 0:
            kcol = red
    if d > dmax:
        dcol = red
    elif dmax / 2 < d < dmax:
        dcol = yellow
    if hungover:
        ecol = purple
        scol = purple
    print(v, ecol, "Энергия =", e, scol, "Связи =", s, kcol, "Кэш =", k, dcol, "Долги =", d, clear)


def MakeGray(text):
    gr = False
    first = True
    for i in range(len(text)):
        if text[i] == '(' and not gr:
            gr = True
            print(grey + text[i], end='')
        elif text[i - 1] == ')' and not text[i] == ')':
            gr = False
            print(clear + text[i], end='')
        elif 115 < i < 125 and first and text[i-1] == ' ':
            print('\n' + text[i], end='')
            first = False
        else:
            print(text[i], end='')


print("-----------------------------------Симулятор студента-----------------------------------")
print('                         Добро пожаловать в симулятор студента!')
print('Скоро у вас сессия и вы как очень порядочный студент ничего не делали и накопили долги.\n'
      'Цель игры - избавиться от долгов (сделать Д <= 0) и не дать остальным параметрам упасть ниже нуля\n'
      'Есть 4 основных параметра: Энергия(Э), Связи(С), Кэш(К)((то бишь деньги)), и, собсна, ' + red + 'ДОЛГИ(Д)\n')
pers = input(clear + "Можете выбрать себе персонажа(ранжированы по сложности):\n"
                     "1. Перваш (объясняются все правила, долгов не очень много, однако связей меньше, чем у остальных."
                     "Много энергии, нет похмелья)\n"
                     "2. Тян (много связей, выше шанс того, что перепадёт или препод простит часть долгов)\n"
                     "3. Дефолтный (Выбирается при любом другом вводе)\n"
                     "4. (не готов)Зубрилка (мало связей, мало долгов, энергии меньше, чем у дефолтного)\n"
                     "5. (не готов)Никита (самый сложный - много долгов, мало времени, выжить нереально)\n")

rules = False
sroki = 15
sexluck = 20

if pers == '1':
    e = 20
    d = 15
    k = 20
    s = 5
    rules = True
elif pers == '2':
    e = 15
    d = 20
    k = 15
    s = 10
    sexluck = 10
elif pers == '4':
    e = 10
    d = 20
    k = 15
    s = 5
elif pers == '5':
    e = 15
    d = 40
    k = 10
    s = 5
    sroki = 10
else:
    e = 15
    d = 30
    k = 15
    s = 5
    sroki = 15
    sexluck = 20

nights = 0
day = 0
kindluck = sexluck
hungover = False
dayafter = False
ups = 'Упс! Такого действия нет. Выберите цифру из предложенных'
hui = input("Поехали? ")

if hui == 'нет':
    print("У вас нет выбора :)")

while d > 0 and e >= 0 and k >= 0 and s >= 0 and nights < sroki:
    print("\nНежного пробуждения! Пора на пары.")
    if day:
        dayafter = False
    elif dayafter:
        s += 10
        e += 10
        day = True
        sexluck = 20
    if hungover:
        print(yellow + "Сегодня у вас похмелье. На один день Энергия и Связи падают на 10" + clear)
        e -= 10
        s -= 10
        day = False
        sexluck = 10
        dayafter = True
    eda = Luck(10)
    sex = Luck(sexluck)
    ill = Luck(20)
    lottery10 = Luck(10)
    lottery100 = Luck(100)
    kind = Luck(kindluck)

    print(green, end='')
    if eda:
        print("УДАЧА! Вам отдали недоеденные пельмени. Энергия+10")
        e += 10
    if sex:
        gay = 'с ' + red + 'м' + yellow + 'у' + green + 'ж' + blue + 'и' + navy + 'к' + purple + 'ом' + green
        if pers == '2':
            gay = 'с ' + red + 'д' + yellow + 'ев' + green + 'у' + blue + 'ш' + navy + 'к' + purple + 'ой' + green
        print('УДАЧА! Вам перепало ' + gay + ' Энергия+20, Связи+20')
        e += 20
        s += 20
    if lottery10:
        print("УДАЧА! Вы выиграли в лотерею 10 денег")
        k += 10
    if lottery100:
        print("ВАМ НЕРЕАЛЬНО ПОВЕЗЛО! Вы выиграли в лотерею 100 денег")
        k += 100
    if kind:
        print("Преподаватель сжалился над вами и простил часть долгов. Долги-5")
        d -= 5
    print(yellow, end='')
    if ill:
        print("НЕУДАЧА! Вы заболели. Энергия-10")
        e -= 10
    print(clear, end='')

    Balance("Ваш баланс:", pers)

    for counter in range(2):
        q = "У вас есть 5 действий: 1. Поесть 2. Учиться 3. Работать 4. Бухать 5. Спать. Введите цифру: "
        if rules:
            q = 'У вас есть 5 действий: 1. Поесть(+Э, (+С)) 2. Учиться(-Д, -Э, (+С)) 3. Работать(-Э, +К, (+С)) ' \
                '4. Бухать(+С, +Э, -К) 5. Спать(+5 Э). Введите цифру: '
        n = Inp(5, ups, q)
        if n == 1:
            q1 = "Вы можете: 1. Купить еду 2. Питаться голубями 3. Есть Чужое "
            if s < 30 and rules:
                q1 = "Вы можете: 1. Купить еду(+10 Э, -10 К) 2. Питаться голубями(+5 Э, -5 С) " \
                     "3. Есть Чужое (пока связи < 30, при выборе данного действия у вас будет -20 энергии) "
            elif rules:
                q1 = "Вы можете: 1. Купить еду(+10 Э, -10 К) 2. Питаться голубями(+5 Э, -5 С) " \
                     "3. Есть Чужое (+10 Э, -5 С) "

            m = Inp(3, ups, q1)
            if m == 1:
                k -= 10
                e += 10
            elif m == 2:
                e += 5
                s -= 5
            elif m == 3:
                if s < 30:
                    print("Ой! У вас недоcтаточно связей для данного действия. Вы лох и теряете энергию xD")
                    e -= 20
                elif s >= 30:
                    s -= 5
                    e += 10

        elif n == 2:
            q2 = "Вы можете учиться: 1. Интенсивно 2. Лениво 3. За компанию " \
                 "4. Дать взятку и погасить 10 долгов (стоит 50 денег) "
            if rules:
                q2 = "Вы можете учиться: 1. Интенсивно(-15 Э, -6 Д) 2. Лениво(-7 Э, -3 Д) 3. За компанию(-5 Э, +5 С, " \
                     "-2 Д) \n4. Дать взятку и погасить 10 долгов (стоит 50 денег) "
            m = Inp(4, ups, q2)
            if m == 1:
                d -= 6
                e -= 15
            elif m == 2:
                d -= 3
                e -= 7
            elif m == 3:
                d -= 2
                s += 5
                e -= 5
            elif m == 4:
                d -= 10
                k -= 50
        elif n == 3:
            q3 = "Вы можете: 1. Помогать кому-то за просто так 2. Помогать кому-то за небольшую плату " \
                 "3. Работать на дядю 4. Работать по блату "
            if rules:
                q3 = "Вы можете: 1. Помогать кому-то за просто так(+10 C, -5 Э) " \
                     "2. Помогать кому-то за небольшую плату(+5 С, -5 Э, +5 К) \n3. Работать на дядю(-20 Э, +20 К) " \
                     "4. Работать по блату(нужны связи >= 30(иначе: -15 С), -5 Э, + 20 К, -5 С) \n"
            m = Inp(4, ups, q3)
            if m == 1:
                s += 10
                e -= 5
            elif m == 2:
                s += 5
                e -= 5
                k += 5
            elif m == 3:
                k += 20
                e -= 20
            elif m == 4:
                if s < 30:
                    print("Вы лох и не можете работать по блату xD")
                    s -= 15
                elif s >= 30:
                    k += 20
                    e -= 5
                    s -= 5
        elif n == 4:
            q4 = "Вы можете пить 1. За компанию 2. Платить за себя "
            if rules:
                q4 = "Вы можете пить 1. За компанию (если связи < 30, -10 Э, -10 С, иначе +10 Э, +5 С, -7 К) " \
                     "2. Платить за себя(-10 K, +10 С, +5 Э) "
            m = Inp(2, ups, q4)
            if m == 1:
                if s < 30:
                    print("Ой! У вас недоcтаточно связей для данного действия. Вы лох и теряете энергию xD")
                    e -= 10
                    s -= 10
                elif s >= 30:
                    e += 10
                    s += 5
                    k -= 7
            elif m == 2:
                k -= 10
                e += 5
                s += 10
        elif n == 5:
            e += 5
        Balance("\nТеперь Ваш баланс:", pers)
    qnight = "\nГород засыпает. Вы хотите учиться, работать или пить всю ночь? 1. Учиться 2. Пить 3. Работать 4. Нет "
    if rules:
        qnight = "\nГород засыпает. Вы хотите учиться, работать или пить всю ночь? 1. Учиться (-10 Э, -4 Д, +5 К) \n" \
                 "2. Пить(+8 С, +2 Д, -8 К) 3. Работать (-10 Э, +15 К) 4.Нет "

    string = Inp(4, "Ответь на вопрос, чепушила ", qnight)
    hungover = False

    if string == 1:
        e -= 10
        d -= 4
        k += 5
    elif string == 2:
        k -= 8
        s += 8
        d += 2
        if not rules:
            hungover = True
    elif string == 3:
        e -= 10
        k += 15
        d += 2
    elif string == 4:
        print("\nЛодыря ответ. Доброй ночи(нет).")
        e += 5
        d += 2
        k += 5

    nights += 1

print(red, end='')

if (e < 0 or s < 0) and dayafter:
    print("\nВы умерли от похмелья!")
else:
    if e < 0:
        print("\nУ вас закончилась энергия и вы пали замертво от усталости!")
    if k < 0:
        print("\nВас случайно убили коллекторы!")
    if nights >= sroki:
        print("\nВы не успели закрыть долги! Здравствуй, небо в облаках!")
    if s <= 0:
        print("\nВы умерли от одиночества и депрессии!")
print(clear, end='')
if d <= 0:
    if 2 <= nights <= 4:
        skl = 'дня'
    elif nights > 4:
        skl = 'дней'
    else:
        skl = 'день'
    print(green, "\nВы погасили все долги за", nights, skl + ". В этом году вы не в армии!", clear)

Balance("Итого:", pers)
