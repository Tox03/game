from tkinter import *  # модуль ткинтер (для создания окон , кнопок , надписей и вцелом работы с окнами созданными им)
from random import *  # модуль рандома (для создания рандомных чисел)
from tkinter import ttk  # подмодуль ткинтера (для создания вкладок и работы с ними)
import time  # модуль времени (для сохранения времени)

# всё ниже перечисленные значения( имена или переменные ) возвращается после перезапуска к значениям указанным ниже (если поменять то к тем на какие они поменяны)
# подсчёт кнопок ведётся сверху вниз и затем слева направо (десята внизу )

maxlevels = 0  # количество максимально прокаченных кнопок
cashforsek = 0  # количество денег в секунду
price = 5000  # цена улучшения количества со сколькольких рандомных кнопок соберётся прибыль (меняется с каждой покупкой)
amountofmoney = 0  # количество собранных денег
cashcollectionamount = 3  # количество со сколькольких рандомных кнопок соберётся прибыль
savetime = 0  # время начала работы игры , а в последующем и начало времени работы cashforsek (может сеняться во время исполнения кода)

cashinbtns_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # список с количеством денег в кнопках
price_lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # цены на улучшение кнопок
addcashinbtn_lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 9]  # количество добавляемой валюты за нажатие на кнопки
upgrades_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # уровень прокачек кнопок
upgradeclick_lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # количесво на которое увеличестся количество приболвяемой прибыли с кнопок при прокачке (меняется с каждой покупкой)
levelmaxupgrade_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # равняется один если кнопка прокаченна на максимум
prisebuyCFS_lst = [64, 576, 5120, 44800, 384000, 3200000, 100000000]
upgradecashforsek_lst = [1, 10, 100, 1000, 10000, 100000]


def updatetext():  # функция обновления текста ( например суммы денег или количества денег в той или иной кнопке)
    global amountofmoney
    global cashinbtns_lst
    lbl.configure(text="собранные деньги = " + str(int(amountofmoney)) + "$")
    lbl1.configure(text="общая сумма денег = " + str(int(sum(cashinbtns_lst) + amountofmoney)) + "$")
    lbl2.configure(text="сумма денег в кнопках = " + str(int(sum(cashinbtns_lst))) + "$")
    lbl3.configure(text="собранные деньги = " + str(int(amountofmoney)) + "$")
    lbl4.configure(text="общая сумма денег = " + str(int(sum(cashinbtns_lst) + amountofmoney)) + "$")
    lbl5.configure(text="сумма денег в кнопках = " + str(int(sum(cashinbtns_lst))) + "$")
    lbl11.configure(text=str(int(cashinbtns_lst[0])) + "$" + " + " + str(int(addcashinbtn_lst[0])) + "$")
    lbl12.configure(text=str(int(cashinbtns_lst[1])) + "$" + " + " + str(int(addcashinbtn_lst[1])) + "$")
    lbl13.configure(text=str(int(cashinbtns_lst[2])) + "$" + " + " + str(int(addcashinbtn_lst[2])) + "$")
    lbl14.configure(text=str(int(cashinbtns_lst[3])) + "$" + " + " + str(int(addcashinbtn_lst[3])) + "$")
    lbl15.configure(text=str(int(cashinbtns_lst[4])) + "$" + " + " + str(int(addcashinbtn_lst[4])) + "$")
    lbl16.configure(text=str(int(cashinbtns_lst[5])) + "$" + " + " + str(int(addcashinbtn_lst[5])) + "$")
    lbl17.configure(text=str(int(cashinbtns_lst[6])) + "$" + " + " + str(int(addcashinbtn_lst[6])) + "$")
    lbl18.configure(text=str(int(cashinbtns_lst[7])) + "$" + " + " + str(int(addcashinbtn_lst[7])) + "$")
    lbl19.configure(text=str(int(cashinbtns_lst[8])) + "$" + " + " + str(int(addcashinbtn_lst[8])) + "$")


def updatetext2():  # функция обновления стоимости услуг , прокачки и денег в секунду
    global levelmaxupgrade_lst
    global maxlevels
    if maxlevels < 18:
        lbl21.configure(text=str(
            min(int(price_lst[0]), int(price_lst[1]), int(price_lst[2]), int(price_lst[3]), int(price_lst[4]),
                int(price_lst[5]), int(price_lst[6]), int(price_lst[7]), int(price_lst[8]))) + " - " + str(
            max(int(price_lst[0]), int(price_lst[1]), int(price_lst[2]), int(price_lst[3]), int(price_lst[4]),
                int(price_lst[5]), int(price_lst[6]), int(price_lst[7]), int(price_lst[8]))) + "$")
        lbl22.configure(text=str(int(price)) + "$")
        lbl23.configure(text=str(int(prisebuyCFS_lst[0])) + "$")
        lbl24.configure(text=str(int(prisebuyCFS_lst[1])) + "$")
        lbl25.configure(text=str(int(prisebuyCFS_lst[2])) + "$")
        lbl26.configure(text=str(int(prisebuyCFS_lst[3])) + "$")
        lbl27.configure(text=str(int(prisebuyCFS_lst[4])) + "$")
        lbl28.configure(text=str(int(prisebuyCFS_lst[5])) + "$")
        lbl29.configure(text=str(int(prisebuyCFS_lst[6])) + "$")
        lbl6.configure(text="+ " + str(int(cashforsek)) + "$ в секунду")
    if levelmaxupgrade_lst[16] == 1 and maxlevels < 18:
        lbl7 = Label(tab1, text=str(int(cashinbtns_lst[9])) + "$" + " + " + str(int(addcashinbtn_lst[9])) + "$",
                     bg="lightblue")
        lbl7.place(x=620, y=672)
        lbl8 = Label(tab2, text=str(int(price_lst[9])) + "$", bg="lightblue")
        lbl8.place(x=620, y=672)


def click1():  # функция нажатия на первую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[0] += addcashinbtn_lst[0]
    updatetext()


def click2():  # функция нажатия на вторую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[1] += addcashinbtn_lst[1]
    updatetext()


def click3():  # функция нажатия на третью кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[2] += addcashinbtn_lst[2]
    updatetext()


def click4():  # функция нажатия на четвёртую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[3] += addcashinbtn_lst[3]
    updatetext()


def click5():  # функция нажатия на пятую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[4] += addcashinbtn_lst[4]
    updatetext()


def click6():  # функция нажатия на шестую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[5] += addcashinbtn_lst[5]
    updatetext()


def click7():  # функция нажатия на седьмую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[6] += addcashinbtn_lst[6]
    updatetext()


def click8():  # функция нажатия на восьмую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[7] += addcashinbtn_lst[7]
    updatetext()


def click9():  # функция нажатия на девятую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[8] += addcashinbtn_lst[8]
    updatetext()


def click10():  # функция нажатия на десятую кнопку
    global cashinbtns_lst
    global addcashinbtn_lst
    cashinbtns_lst[9] += addcashinbtn_lst[9]
    updatetext()


def upgrades():  # функция прокачки кнопок
    global amountofmoney
    global price_lst
    global addcashinbtn_lst
    global upgradeclick_lst
    global cashforsek
    global levelmaxupgrade_lst
    global maxlevels
    global upgrades_lst
    randomnamber = randint(0, 8)
    if price_lst[randomnamber] < amountofmoney and levelmaxupgrade_lst[16] == 0 and upgrades_lst[randomnamber] < 25:
        amountofmoney -= price_lst[randomnamber]
        price_lst[randomnamber] *= 1.8
        addcashinbtn_lst[randomnamber] += upgradeclick_lst[randomnamber]
        addcashinbtn_lst[9] += upgradeclick_lst[randomnamber] / 100
        upgradeclick_lst[randomnamber] *= 1.5
        upgrades_lst[randomnamber] += 1
        if (upgrades_lst[randomnamber] == 25 or upgrades_lst[randomnamber] > 25) and levelmaxupgrade_lst[
            randomnamber] == 0:
            levelmaxupgrade_lst[randomnamber] = 1
    else:
        if price_lst[randomnamber] < amountofmoney and levelmaxupgrade_lst[16] == 1 and upgrades_lst[randomnamber] < 25:
            amountofmoney -= price_lst[randomnamber]
            price_lst[randomnamber] *= 1.8
            cashforsek += upgradeclick_lst[randomnamber]
            addcashinbtn_lst[9] += upgradeclick_lst[randomnamber] / 100
            upgradeclick_lst[randomnamber] *= 1.5
            upgrades_lst[randomnamber] += 1
            if (upgrades_lst[randomnamber] == 25 or upgrades_lst[randomnamber] > 25) and levelmaxupgrade_lst[
                randomnamber] == 0:
                levelmaxupgrade_lst[randomnamber] = 1
        else:
            for number08 in range(0, 9):
                if price_lst[number08] < amountofmoney and levelmaxupgrade_lst[16] == 0 and upgrades_lst[number08] < 25:
                    amountofmoney -= price_lst[number08]
                    price_lst[number08] *= 1.8
                    addcashinbtn_lst[number08] += upgradeclick_lst[number08]
                    addcashinbtn_lst[9] += upgradeclick_lst[number08] / 100
                    upgradeclick_lst[number08] *= 1.5
                    upgrades_lst[number08] += 1
                    if (upgrades_lst[number08] == 25 or upgrades_lst[number08] > 25) and levelmaxupgrade_lst[number08] == 0:
                        levelmaxupgrade_lst[number08] = 1
                    break
                elif price_lst[number08] < amountofmoney and levelmaxupgrade_lst[16] == 1 and upgrades_lst[number08] < 25:
                    amountofmoney -= price_lst[number08]
                    price_lst[number08] *= 1.8
                    cashforsek += upgradeclick_lst[number08]
                    addcashinbtn_lst[9] += upgradeclick_lst[number08] / 100
                    upgradeclick_lst[number08] *= 1.5
                    upgrades_lst[number08] += 1
                    if (upgrades_lst[number08] == 25 or upgrades_lst[number08] > 25) and levelmaxupgrade_lst[number08] == 0:
                        levelmaxupgrade_lst[number08] = 1
                    break
    updatetext()
    updatetext2()


def upgrade10():  # функция прокачки десятой кнопки
    global amountofmoney
    global price_lst
    global addcashinbtn_lst
    global upgradeclick_lst
    global upgrades_lst
    global levelmaxupgrade_lst
    global maxlevels
    if price_lst[9] < amountofmoney and upgrades_lst[9] < 25:
        amountofmoney -= price_lst[9]
        price_lst[9] *= 1.8
        addcashinbtn_lst[9] += upgradeclick_lst[9]
        upgradeclick_lst[9] *= 1.5
        upgrades_lst[9] += 1
    if (upgrades_lst[9] == 25 or upgrades_lst[9] > 25) and levelmaxupgrade_lst[9] == 0:
        levelmaxupgrade_lst[9] = 1
        maxlevels += 1
    updatetext()
    updatetext2()


def upgrade0():  # функция прокачки количества со сколькольких рандомных кнопок соберётся прибыль
    global amountofmoney
    global price
    global cashcollectionamount
    if price < amountofmoney and cashcollectionamount <= 8:
        amountofmoney -= price
        price *= 2
        cashcollectionamount += 1
    updatetext()
    updatetext2()


def savetimetime():  # обновляет сохранённое время и сохраняет текущее
    global savetime
    savetime = time.time()


def buy1():  # прокачка дохода в секунду на 1 сек
    global amountofmoney
    global prisebuyCFS_lst
    global upgradecashforsek_lst
    global cashforsek
    global savetime
    global maxlevels
    global upgrades_lst
    global levelmaxupgrade_lst
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    if prisebuyCFS_lst[0] < amountofmoney and upgrades_lst[10] < 25:
        amountofmoney -= prisebuyCFS_lst[0]
        prisebuyCFS_lst[0] *= 1.2 * 1.2
        cashforsek += upgradecashforsek_lst[0]
        upgrades_lst[10] += 1
    if (upgrades_lst[10] == 25 or upgrades_lst[10] > 25) and levelmaxupgrade_lst[10] == 0:
        levelmaxupgrade_lst[10] = 1
        maxlevels += 1
    updatetext()
    updatetext2()


def buy2():  # прокачка дохода в секунду на 10 сек
    global amountofmoney
    global prisebuyCFS_lst
    global upgradecashforsek_lst
    global cashforsek
    global savetime
    global maxlevels
    global upgrades_lst
    global levelmaxupgrade_lst
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    if prisebuyCFS_lst[1] < amountofmoney and upgrades_lst[11] < 20:
        amountofmoney -= prisebuyCFS_lst[1]
        prisebuyCFS_lst[1] *= 1.2 * 1.2
        cashforsek += upgradecashforsek_lst[1]
        upgrades_lst[11] += 1
    if (upgrades_lst[11] == 20 or upgrades_lst[11] > 20) and levelmaxupgrade_lst[11] == 0:
        levelmaxupgrade_lst[11] = 1
        maxlevels += 1
    updatetext()
    updatetext2()


def buy3():  # прокачка дохода в секунду на 100 сек
    global amountofmoney
    global prisebuyCFS_lst
    global upgradecashforsek_lst
    global cashforsek
    global savetime
    global maxlevels
    global upgrades_lst
    global levelmaxupgrade_lst
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    if prisebuyCFS_lst[2] < amountofmoney and upgrades_lst[12] < 15:
        amountofmoney -= prisebuyCFS_lst[2]
        prisebuyCFS_lst[2] *= 1.2 * 1.2
        cashforsek += upgradecashforsek_lst[2]
        upgrades_lst[12] += 1
    if (upgrades_lst[12] == 15 or upgrades_lst[12] > 15) and levelmaxupgrade_lst[12] == 0:
        levelmaxupgrade_lst[12] = 1
        maxlevels += 1
    updatetext()
    updatetext2()


def buy4():  # прокачка дохода в секунду на 1000 сек
    global amountofmoney
    global prisebuyCFS_lst
    global upgradecashforsek_lst
    global cashforsek
    global savetime
    global maxlevels
    global upgrades_lst
    global levelmaxupgrade_lst
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    if prisebuyCFS_lst[3] < amountofmoney and upgrades_lst[13] < 15:
        amountofmoney -= prisebuyCFS_lst[3]
        prisebuyCFS_lst[3] *= 1.2 * 1.2
        cashforsek += upgradecashforsek_lst[3]
        upgrades_lst[13] += 1
    if (upgrades_lst[13] == 15 or upgrades_lst[13] > 15) and levelmaxupgrade_lst[13] == 0:
        levelmaxupgrade_lst[13] = 1
        maxlevels += 1
    updatetext()
    updatetext2()


def buy5():  # прокачка дохода в секунду на 10000 сек
    global amountofmoney
    global prisebuyCFS_lst
    global upgradecashforsek_lst
    global cashforsek
    global savetime
    global maxlevels
    global upgrades_lst
    global levelmaxupgrade_lst
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    if prisebuyCFS_lst[4] < amountofmoney and upgrades_lst[14] < 10:
        amountofmoney -= prisebuyCFS_lst[4]
        prisebuyCFS_lst[4] *= 1.2 * 1.2
        cashforsek += upgradecashforsek_lst[4]
        upgrades_lst[14] += 1
    if (upgrades_lst[14] == 10 or upgrades_lst[14] > 10) and levelmaxupgrade_lst[14] == 0:
        levelmaxupgrade_lst[14] = 1
        maxlevels += 1
    updatetext()
    updatetext2()


def buy6():  # прокачка дохода в секунду на 100000 сек
    global amountofmoney
    global prisebuyCFS_lst
    global upgradecashforsek_lst
    global cashforsek
    global savetime
    global maxlevels
    global upgrades_lst
    global levelmaxupgrade_lst
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    if prisebuyCFS_lst[5] < amountofmoney and upgrades_lst[15] < 5:
        amountofmoney -= prisebuyCFS_lst[5]
        prisebuyCFS_lst[5] *= 1.2 * 1.2
        cashforsek += upgradecashforsek_lst[5]
        upgrades_lst[15] += 1
    if (upgrades_lst[15] == 5 or upgrades_lst[15] > 5) and levelmaxupgrade_lst[15] == 0:
        levelmaxupgrade_lst[15] = 1
        maxlevels += 1
    updatetext()
    updatetext2()


def buy7():  # прокачка дохода в сек на количество прибыли со всех кнопок кроме 10
    global amountofmoney
    global prisebuyCFS_lst
    global cashforsek
    global savetime
    global maxlevels
    global levelmaxupgrade_lst
    global addcashinbtn_lst
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    if prisebuyCFS_lst[6] < amountofmoney and levelmaxupgrade_lst[16] == 0:
        cashforsek = cashforsek + (
                    addcashinbtn_lst[0] + addcashinbtn_lst[1] + addcashinbtn_lst[2] + addcashinbtn_lst[3] +
                    addcashinbtn_lst[4] + addcashinbtn_lst[5] + addcashinbtn_lst[6] + addcashinbtn_lst[7] +
                    addcashinbtn_lst[8])
        addcashinbtn_lst[0] = 0
        addcashinbtn_lst[1] = 0
        addcashinbtn_lst[2] = 0
        addcashinbtn_lst[3] = 0
        addcashinbtn_lst[4] = 0
        addcashinbtn_lst[5] = 0
        addcashinbtn_lst[6] = 0
        addcashinbtn_lst[7] = 0
        addcashinbtn_lst[8] = 0
        amountofmoney -= prisebuyCFS_lst[6]
        levelmaxupgrade_lst[16] = 1
        maxlevels += 1
        plusbutton()
    updatetext()
    updatetext2()


def plusbutton():  # функция добавления 10 кнопки , и её прокачки , а так-же текст под ними
    btn10 = Button(tab1, text="клик", command=click10, width=67, height=4, bg="pink", fg="blue")
    btn10.place(x=400, y=600)
    btn11 = Button(tab2, text="улучшение 10 кнопки", command=upgrade10, width=67, height=4, bg="pink", fg="blue")
    btn11.place(x=400, y=600)


def click0():  # Сбор с кликеров и дохода в секунду
    global cashinbtns_lst
    global amountofmoney
    global cashcollectionamount
    global cashforsek
    global savetime
    seks = time.time() - savetime
    amountofmoney += seks * cashforsek
    savetimetime()
    numbers08v1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    lenofnumbers08 = 9
    amountofmoney += cashinbtns_lst[9]
    cashinbtns_lst[9] = 0
    if cashcollectionamount == 9 or cashcollectionamount > 9:
        amountofmoney += sum(cashinbtns_lst)
        cashinbtns_lst[0] = 0
        cashinbtns_lst[1] = 0
        cashinbtns_lst[2] = 0
        cashinbtns_lst[3] = 0
        cashinbtns_lst[4] = 0
        cashinbtns_lst[5] = 0
        cashinbtns_lst[6] = 0
        cashinbtns_lst[7] = 0
        cashinbtns_lst[8] = 0
    else:
        for number in range(cashcollectionamount):
            lenofnumbers08 -= 1
            numbers08v2 = []
            randomnamber0lon = randint(0, lenofnumbers08)
            amountofmoney += cashinbtns_lst[numbers08v1[randomnamber0lon]]
            cashinbtns_lst[numbers08v1[randomnamber0lon]] = 0
            numbers08v1[randomnamber0lon] = ""
            for i in numbers08v1:
                if i != "":
                    numbers08v2.append(number)
            numbers08v1 = numbers08v2
    updatetext()
    updatetext2()


savetimetime()

# создание окна , покраска заднего фона и вкладок
window = Tk()
window.title("кликер 339")
window.geometry("1000x800")
window.config(bg="lightblue")
tab_control = ttk.Notebook(window)
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab0, text="инструкция")
tab_control.add(tab1, text="кликер")
tab_control.add(tab2, text="улучшения")
tab_control.pack(expand=1, fill="both")
ttk.Style().configure("TFrame", background="lightblue")

# текст на первой вкладке
lbl51 = Label(tab0, text="Это игра - кликер. Вверху есть 3 вкладки про них читай ниже.", bg="lightblue",
              font=("Arial Bold", 15), height=3)
lbl51.grid(column=0, row=0)
lbl52 = Label(tab0, text="Первая вкладка - инструкция, здесь всё понятно", bg="lightblue", font=("Arial Bold", 15),
              height=3)
lbl52.grid(column=0, row=1)
lbl53 = Label(tab0, text="Вторая вкладка - кликер, есть 10 кнопок , из них  9 кликеров и 1 кнопка сбора про них ниже .",
              bg="lightblue", font=("Arial Bold", 15), height=3)
lbl53.grid(column=0, row=2)
lbl54 = Label(tab0, text="Кликеры - нажимай и прокачийвай их на следующей вкладке", bg="lightblue",
              font=("Arial Bold", 15), height=3)
lbl54.grid(column=0, row=3)
lbl55 = Label(tab0, text="Кнопка сбора - собирает прибыль со скольких-то рандомно выбранных кликеров ( вначале с 3) ",
              bg="lightblue", font=("Arial Bold", 15), height=3)
lbl55.grid(column=0, row=4)
lbl56 = Label(tab0,
              text="Третья вкладка - прокачка, есть 9 кнопок ,из них 7 прокачек зароботка в секунду , одна прокачивает ",
              bg="lightblue", font=("Arial Bold", 15), height=3)
lbl56.grid(column=0, row=5)
lbl57 = Label(tab0, text=" кнопки , а ещё одна увеличивает количество рандомно выбранных кликеров для сбора кликеров",
              bg="lightblue", font=("Arial Bold", 15), height=3)
lbl57.grid(column=0, row=6)
lbl58 = Label(tab0,
              text="Заработок в секунду не собирается автоматически , для его сбора нужно нажать на кнопку сбора ",
              bg="lightblue", font=("Arial Bold", 15), height=3)
lbl58.grid(column=0, row=7)
lbl58 = Label(tab0,
              text="Так-же прокачка девятой кнопки добавляет заработок в сек равный сумме добавления денег в каждую из кнопок ",
              bg="lightblue", font=("Arial Bold", 14), height=3)
lbl58.grid(column=0, row=8)

# текст на второй вкладке
lbl = Label(tab1, text="собранные деньги = " + str(amountofmoney) + "$", bg="lightgreen")
lbl.place(x=10, y=30)
lbl1 = Label(tab1, text="общая сумма денег = " + str(sum(cashinbtns_lst) + amountofmoney) + "$", bg="lightgreen")
lbl1.place(x=10, y=50)
lbl2 = Label(tab1, text="сумма денег в кнопках = " + str(sum(cashinbtns_lst)) + "$", bg="lightgreen")
lbl2.place(x=10, y=70)
lbl6 = Label(tab1, text="+ " + str(cashforsek) + "$ в секунду", bg="lightgreen")
lbl6.place(x=10, y=90)
lbl11 = Label(tab1, text=str(cashinbtns_lst[0]) + "$" + " + " + str(addcashinbtn_lst[0]) + "$", bg="lightblue")
lbl11.place(x=400, y=370)
lbl12 = Label(tab1, text=str(cashinbtns_lst[1]) + "$" + " + " + str(addcashinbtn_lst[1]) + "$", bg="lightblue")
lbl12.place(x=400, y=470)
lbl13 = Label(tab1, text=str(cashinbtns_lst[2]) + "$" + " + " + str(addcashinbtn_lst[2]) + "$", bg="lightblue")
lbl13.place(x=400, y=570)
lbl14 = Label(tab1, text=str(cashinbtns_lst[3]) + "$" + " + " + str(addcashinbtn_lst[3]) + "$", bg="lightblue")
lbl14.place(x=600, y=370)
lbl15 = Label(tab1, text=str(cashinbtns_lst[4]) + "$" + " + " + str(addcashinbtn_lst[4]) + "$", bg="lightblue")
lbl15.place(x=600, y=470)
lbl16 = Label(tab1, text=str(cashinbtns_lst[5]) + "$" + " + " + str(addcashinbtn_lst[5]) + "$", bg="lightblue")
lbl16.place(x=600, y=570)
lbl17 = Label(tab1, text=str(cashinbtns_lst[6]) + "$" + " + " + str(addcashinbtn_lst[6]) + "$", bg="lightblue")
lbl17.place(x=800, y=370)
lbl18 = Label(tab1, text=str(cashinbtns_lst[7]) + "$" + " + " + str(addcashinbtn_lst[7]) + "$", bg="lightblue")
lbl18.place(x=800, y=470)
lbl19 = Label(tab1, text=str(cashinbtns_lst[8]) + "$" + " + " + str(addcashinbtn_lst[8]) + "$", bg="lightblue")
lbl19.place(x=800, y=570)

# текст на третей вкладке
lbl3 = Label(tab2, text="собранные деньги = " + str(amountofmoney) + "$", bg="lightgreen")
lbl3.place(x=10, y=30)
lbl4 = Label(tab2, text="общая сумма денег = " + str(sum(cashinbtns_lst) + amountofmoney) + "$", bg="lightgreen")
lbl4.place(x=10, y=50)
lbl5 = Label(tab2, text="сумма денег в кнопках = " + str(sum(cashinbtns_lst)) + "$", bg="lightgreen")
lbl5.place(x=10, y=70)
lbl21 = Label(tab2,
              text=str(
                  min(price_lst[0], price_lst[1], price_lst[2], price_lst[3], price_lst[4], price_lst[5], price_lst[6],
                      price_lst[7], price_lst[8])) + "$" + " - " + str(
                  max(price_lst[0], price_lst[1], price_lst[2], price_lst[3], price_lst[4], price_lst[5], price_lst[6],
                      price_lst[7], price_lst[8])) + "$", bg="lightblue")
lbl21.place(x=400, y=370)
lbl22 = Label(tab2, text=str(price) + "$", bg="lightblue")
lbl22.place(x=400, y=470)
lbl23 = Label(tab2, text=str(prisebuyCFS_lst[0]) + "$", bg="lightblue")
lbl23.place(x=400, y=570)
lbl24 = Label(tab2, text=str(prisebuyCFS_lst[1]) + "$", bg="lightblue")
lbl24.place(x=600, y=370)
lbl25 = Label(tab2, text=str(prisebuyCFS_lst[2]) + "$", bg="lightblue")
lbl25.place(x=600, y=470)
lbl26 = Label(tab2, text=str(prisebuyCFS_lst[3]) + "$", bg="lightblue")
lbl26.place(x=600, y=570)
lbl27 = Label(tab2, text=str(prisebuyCFS_lst[4]) + "$", bg="lightblue")
lbl27.place(x=800, y=370)
lbl28 = Label(tab2, text=str(prisebuyCFS_lst[5]) + "$", bg="lightblue")
lbl28.place(x=800, y=470)
lbl29 = Label(tab2, text=str(prisebuyCFS_lst[6]) + "$", bg="lightblue")
lbl29.place(x=800, y=570)

# кнопки на второй вкладке
btn1 = Button(tab1, text="клик", command=click1, width=10, height=4, bg="pink", fg="blue")
btn1.place(x=400, y=300)
btn2 = Button(tab1, text="клик", command=click2, width=10, height=4, bg="pink", fg="blue")
btn2.place(x=400, y=400)
btn3 = Button(tab1, text="клик", command=click3, width=10, height=4, bg="pink", fg="blue")
btn3.place(x=400, y=500)
btn4 = Button(tab1, text="клик", command=click4, width=10, height=4, bg="pink", fg="blue")
btn4.place(x=600, y=300)
btn5 = Button(tab1, text="клик", command=click5, width=10, height=4, bg="pink", fg="blue")
btn5.place(x=600, y=400)
btn6 = Button(tab1, text="клик", command=click6, width=10, height=4, bg="pink", fg="blue")
btn6.place(x=600, y=500)
btn7 = Button(tab1, text="клик", command=click7, width=10, height=4, bg="pink", fg="blue")
btn7.place(x=800, y=300)
btn8 = Button(tab1, text="клик", command=click8, width=10, height=4, bg="pink", fg="blue")
btn8.place(x=800, y=400)
btn9 = Button(tab1, text="клик", command=click9, width=10, height=4, bg="pink", fg="blue")
btn9.place(x=800, y=500)
btn0 = Button(tab1, text="собрать", command=click0, width=10, height=4, bg="lightgreen", fg="blue")
btn0.place(x=600, y=100)

# кнопки на третей вкладке
btnup1 = Button(tab2, text="улучшение", command=upgrades, width=10, height=4, bg="pink", fg="blue")
btnup1.place(x=400, y=300)
btnup2 = Button(tab2, text="+ 1 рабочий", command=upgrade0, width=10, height=4, bg="pink", fg="blue")
btnup2.place(x=400, y=400)
btnup3 = Button(tab2, text="+" + str(upgradecashforsek_lst[0]) + "$" + " в сек", command=buy1, width=10, height=4,
                bg="pink",
                fg="blue")
btnup3.place(x=400, y=500)
btnup4 = Button(tab2, text="+" + str(upgradecashforsek_lst[1]) + "$" + " в сек", command=buy2, width=10, height=4,
                bg="pink",
                fg="blue")
btnup4.place(x=600, y=300)
btnup5 = Button(tab2, text="+" + str(upgradecashforsek_lst[2]) + "$" + " в сек", command=buy3, width=10, height=4,
                bg="pink",
                fg="blue")
btnup5.place(x=600, y=400)
btnup6 = Button(tab2, text="+" + str(upgradecashforsek_lst[3]) + "$" + " в сек", command=buy4, width=10, height=4,
                bg="pink",
                fg="blue")
btnup6.place(x=600, y=500)
btnup7 = Button(tab2, text="+" + str(upgradecashforsek_lst[4]) + "$" + " в сек", command=buy5, width=10, height=4,
                bg="pink",
                fg="blue")
btnup7.place(x=800, y=300)
btnup8 = Button(tab2, text="+" + str(upgradecashforsek_lst[5]) + "$" + " в сек", command=buy6, width=10, height=4,
                bg="pink",
                fg="blue")
btnup8.place(x=800, y=400)
btnup9 = Button(tab2, text="+" + "???" + "$" + " в сек", command=buy7, width=10, height=4, bg="pink", fg="blue")
btnup9.place(x=800, y=500)

window.mainloop()  # функция "запуска" модуля ткинтер