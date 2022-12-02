import random
from dataclasses import dataclass

red = '\033[31m'
yellow = '\033[33m'
green = '\033[32m'
blue = '\033[36m'
navy = '\033[34m'
purple = '\033[35m'
grey = '\033[37m'
black = '\033[30m'
clear = '\033[0m'


@dataclass
class Person:
    name: str = '3'
    e: int = 15
    s: int = 5
    k: int = 15
    d: int = 30
    sexluck: int = 20
    sroki: int = 10
    sex: str = 'm'
    mayhungover: bool = True
    rules: bool = False
    hungover: bool = False
    day: bool = False
    dayafter: bool = False


def luck(value):
    a1 = random.randint(1, value)
    a2 = random.randint(1, value)
    if a1 == a2:
        return True

    return False


def inp(v, ifnot, quest):
    ans = input(makegray(quest))
    if ans == 'назад':
        if v == 5:
            if actioncount == 0:
                nazad = True
            else:
                nazad = False
        else:
            nazad = True
    else:
        nazad = False
    while ans != str(v) and ans != str(v - 1) and ans != str(v - 2) and ans != str(v - 3) and ans != str(v - 4) \
            and not nazad:
        print(ifnot)
        ans = input(makegray(quest))
        if ans == 'назад':
            nazad = True
    if not nazad:
        xyu = int(ans)
    else:
        xyu = ans
    return xyu


def balance(v):
    ecol = green
    scol = green
    kcol = green
    dcol = green

    if pers.e < 10:
        ecol = yellow
        if pers.e < 0:
            ecol = red
    if pers.s < 10:
        scol = yellow
        if pers.s < 0:
            scol = red
    if pers.k < 10:
        kcol = yellow
        if pers.k < 0:
            kcol = red
    if pers.d > d:
        dcol = red
    elif d / 2 < pers.d < d:
        dcol = yellow
    if pers.dayafter and pers.mayhungover:
        ecol = purple
        scol = purple
    print(v, ecol, "Энергия =", pers.e, scol, "Связи =", pers.s, kcol, "Кэш =", pers.k, dcol, "Долги =", pers.d, clear)


def makegray(text):
    gr = False
    for i in range(len(text)):
        if text[i] == '(' and not gr:
            gr = True
            print(grey + text[i], end='')
        elif text[i - 1] == ')' and not text[i] == ')':
            gr = False
            print(clear + text[i], end='')
        else:
            print(text[i], end='')

    return ''


def funname():
    name = input(clear + "Можете выбрать себе персонажа(ранжированы по сложности):\n"
                         "1. Перваш (объясняются все правила, долгов не очень много, однако связей меньше,"
                         " чем у остальных."
                         "Много энергии, нет похмелья)\n"
                         "2. Тян (много связей, выше шанс того, что перепадёт или препод простит часть долгов)\n"
                         "3. Дефолтный (Выбирается при любом другом вводе)\n"
                         "4. Зубрилка (мало связей, мало долгов, ниже шанс, что перепадёт, "
                         "энергии меньше, чем у дефолтного)\n"
                         "5. Никита (самый сложный - много долгов, мало денег, выжить нереально)\n")
    if name == '1':
        perso = Person(name, 20, k=20, d=10, sroki=15, rules=True)
    elif name == '2':
        perso = Person(name, s=10, sexluck=10, sex='w')
    elif name == '4':
        perso = Person(name, 10, 0, d=20, sexluck=30)
    elif name == '5':
        perso = Person(name, 10, k=10, d=40)
    else:
        perso = Person()

    poehali()

    return perso


def poehali():
    hui = input("Поехали? ")
    if hui == 'нет':
        print("У вас нет выбора :)")
    elif hui == 'иди нахуй':
        print('Сам иди')
        pers.sexluck = 1000000
    elif hui == 'да':
        print('Это был риторический вопрос.')
    elif hui == 'назад':
        funname()


def utro():
    print("\nНежного пробуждения! Пора на пары.")
    if pers.dayafter:
        pers.dayafter = False
        if pers.mayhungover:
            pers.s += 10
            pers.e += 10
        if sexluck == 20:
            pers.sexluck = 20
    if pers.hungover:
        pers.sexluck = 10
        pers.dayafter = True
        pers.hungover = False
        if pers.mayhungover:
            print(yellow + "Сегодня у вас похмелье. На один день Энергия и Связи падают на 10" + clear)
            pers.e -= 10
            pers.s -= 10

    eda = luck(10)
    got = luck(pers.sexluck)
    ill = luck(20)
    lottery10 = luck(10)
    lottery100 = luck(100)
    kind = luck(kindluck)
    dr = luck(365)

    print(green, end='')
    if eda:
        print("УДАЧА! Вам отдали недоеденные пельмени. Энергия+10")
        pers.e += 10
    if got:
        if pers.sex == 'm':
            gay = 'с ' + red + 'м' + yellow + 'у' + green + 'ж' + blue + 'и' + navy + 'к' + purple + 'ом' + green
            if pers.sex == 'w':
                gay = 'с ' + red + 'д' + yellow + 'ев' + green + 'у' + blue + 'ш' + navy + 'к' + purple + 'ой' + green
            print('УДАЧА! Вам перепало ' + gay + ' Энергия+20, Связи+20')
            pers.e += 20
            pers.s += 20
    if lottery10:
        print("УДАЧА! Вы выиграли в лотерею 10 денег")
        pers.k += 10
    if lottery100:
        print("ВАМ НЕРЕАЛЬНО ПОВЕЗЛО! Вы выиграли в лотерею 100 денег")
        pers.k += 100
    if kind:
        print("Преподаватель сжалился над вами и простил часть долгов. Долги-5")
        pers.d -= 5
    if dr:
        print("Сегодня у вас день рождения! Кэш+20, Энергия+20, Связи+20")
        pers.k += 20
        pers.e += 20
        pers.s += 20
    print(yellow, end='')
    if ill:
        print("НЕУДАЧА! Вы заболели. Энергия-10")
        pers.e -= 10
    print(clear, end='')

    balance("Ваш баланс:")


def funq():
    q = "У вас есть 5 действий: 1. Поесть 2. Учиться 3. Работать 4. Бухать 5. Спать. Введите цифру: "
    if pers.rules:
        q = 'У вас есть 5 действий: 1. Поесть(+Э, (+С)) 2. Учиться(-Д, -Э, (+С)) 3. Работать(-Э, +К, (+С)) \n' \
            '4. Бухать(+С, +Э, -К) 5. Спать(+5 Э). Введите цифру: '
    n1 = inp(5, ups, q)
    funquestion(n1)


def funquestion(n):
    if n == 1:
        funq1()
    elif n == 2:
        funq2()
    elif n == 3:
        funq3()
    elif n == 4:
        funq4()
    elif n == 5:
        funq5()
    elif n == 'назад':
        poehali()
        utro()
        funq()


def funq1():
    q1 = "Вы можете: 1. Купить еду 2. Питаться голубями 3. Есть Чужое "
    if pers.s < 30 and pers.rules:
        q1 = "Вы можете: 1. Купить еду(+10 Э, -10 К) 2. Питаться голубями(+5 Э, -5 С) \n" \
             "3. Есть Чужое (пока связи < 30, при выборе данного действия у вас будет -20 энергии) "
    elif pers.rules:
        q1 = "Вы можете: 1. Купить еду(+10 Э, -10 К) 2. Питаться голубями(+5 Э, -5 С) \n" \
             "3. Есть Чужое (+10 Э, -5 С) "

    m = inp(3, ups, q1)
    if m == 1:
        pers.k -= 10
        pers.e += 10
    elif m == 2:
        pers.e += 5
        pers.s -= 5
    elif m == 3:
        if pers.s < 30:
            print("Ой! У вас недоcтаточно связей для данного действия. Вы лох и теряете энергию xD")
            pers.e -= 20
        elif pers.s >= 30:
            pers.s -= 5
            pers.e += 10
    elif m == 'назад':
        funq()


def funq2():
    q2 = "Вы можете учиться: 1. Интенсивно 2. Лениво 3. За компанию \n" \
         "4. Дать взятку и погасить 10 долгов (стоит 50 денег) "
    if pers.rules:
        q2 = "Вы можете учиться: 1. Интенсивно(-15 Э, -9 Д) 2. Лениво(-7 Э, -3 Д) 3. За компанию(-5 Э, +5 С, " \
             "-2 Д) \n4. Дать взятку и погасить 10 долгов (стоит 50 денег) "
    m = inp(4, ups, q2)
    if m == 1:
        pers.d -= 6
        pers.e -= 15
    elif m == 2:
        pers.d -= 3
        pers.e -= 7
    elif m == 3:
        pers.d -= 2
        pers.s += 5
        pers.e -= 5
    elif m == 4:
        pers.d -= 10
        pers.k -= 50
    elif m == 'назад':
        funq()


def funq3():
    q3 = "Вы можете: 1. Помогать кому-то за просто так 2. Помогать кому-то за небольшую плату \n" \
         "3. Работать на дядю 4. Работать по блату "
    if pers.rules:
        q3 = "Вы можете: 1. Помогать кому-то за просто так(+10 C, -5 Э) " \
             "2. Помогать кому-то за небольшую плату(+5 С, -5 Э, +5 К) \n3. Работать на дядю(-20 Э, +20 К) " \
             "4. Работать по блату(нужны связи >= 30(иначе: -15 С), -5 Э, + 20 К, -5 С) \n"
    m = inp(4, ups, q3)
    if m == 1:
        pers.s += 10
        pers.e -= 5
    elif m == 2:
        pers.s += 5
        pers.e -= 5
        pers.k += 5
    elif m == 3:
        pers.k += 20
        pers.e -= 20
    elif m == 4:
        if pers.s < 30:
            print("Вы лох и не можете работать по блату xD")
            pers.s -= 15
        elif pers.s >= 30:
            pers.k += 20
            pers.e -= 5
            pers.s -= 5
    elif m == 'назад':
        funq()


def funq4():
    q4 = "Вы можете пить 1. За компанию 2. Платить за себя "
    if pers.rules:
        q4 = "Вы можете пить 1. За компанию (если связи < 30, -10 Э, -10 С, иначе +10 Э, +5 С, -7 К) \n" \
             "2. Платить за себя(-10 K, +10 С, +5 Э) "
    m = inp(2, ups, q4)
    if m == 1:
        if pers.s < 30:
            print("Ой! У вас недоcтаточно связей для данного действия. Вы лох и теряете энергию xD")
            pers.e -= 10
            pers.s -= 10
        elif pers.s >= 30:
            pers.e += 10
            pers.s += 5
            pers.k -= 7
    elif m == 2:
        pers.k -= 10
        pers.e += 5
        pers.s += 10
    elif m == 'назад':
        funq()


def funq5():
    pers.e += 5


def night():
    qnight = "\nГород засыпает. Вы хотите учиться, работать или пить всю ночь? 1. Учиться 2. Пить 3. Работать 4. Нет "
    if pers.rules:
        qnight = "\nГород засыпает. Вы хотите учиться, работать или пить всю ночь? 1. Учиться (-10 Э, -4 Д, +5 К) \n" \
                 "2. Пить(+8 С, +2 Д, -8 К) 3. Работать (-10 Э, +15 К) 4.Нет "

    string = inp(4, "Ответь на вопрос, чепушила ", qnight)
    pers.hungover = False

    if string == 1:
        pers.e -= 10
        pers.d -= 4
        pers.k += 5
    elif string == 2:
        pers.k -= 8
        pers.s += 8
        pers.d += 2
        pers.hungover = True
    elif string == 3:
        pers.e -= 10
        pers.k += 15
        pers.d += 2
    elif string == 4:
        print("\nЛодыря ответ. Доброй ночи(нет).")
        pers.e += 7
        pers.d += 2
        pers.k += 5


print("-----------------------------------Симулятор студента-----------------------------------")
print('                         Добро пожаловать в симулятор студента!')
print('Скоро у вас сессия и вы как очень порядочный студент ничего не делали и накопили долги.\n'
      'Цель игры - за 10 дней избавиться от долгов (сделать Д <= 0) и не дать остальным параметрам упасть ниже нуля\n'
      'Есть 4 основных параметра: Энергия(Э), Связи(С), Кэш(К)((то бишь деньги)), и, собсна, ' + red + 'ДОЛГИ(Д)\n')

pers = funname()

ups = 'Упс! Такого действия нет. Выберите цифру из предложенных'

actioncount = 0
nights = 0
e = pers.e
s = pers.s
k = pers.k
d = pers.d
sexluck = pers.sexluck
kindluck = sexluck
print(green, "Обновление: теперь вы можете в некоторых случаях возвращаться назад, введя команду 'назад'", clear)

while pers.d > 0 and pers.e >= 0 and pers.k >= 0 and pers.s >= 0 and nights < pers.sroki:
    utro()

    for counter in range(2):
        funq()
        actioncount += 1
        balance("\nТеперь Ваш баланс:")
    night()

    nights += 1


print(red, end='')

if (pers.e < 0 or pers.s < 0) and pers.dayafter and not pers.rules:
    print("\nВы умерли от похмелья!")
else:
    if pers.e < 0:
        print("\nУ вас закончилась энергия и вы пали замертво от усталости!")
    if pers.k < 0:
        print("\nВас случайно убили коллекторы!")
    if nights > pers.sroki:
        print("\nВы не успели закрыть долги! Здравствуй, небо в облаках!")
    if pers.s <= 0:
        print("\nВы умерли от одиночества и депрессии!")
print(clear, end='')
if pers.d <= 0:
    if 2 <= nights <= 4:
        skl = 'дня'
    elif nights > 4:
        skl = 'дней'
    else:
        skl = 'день'
    print(green, "\nВы погасили все долги за", nights, skl + ". В этом году вы не в армии!", clear)

balance("Итого:")
