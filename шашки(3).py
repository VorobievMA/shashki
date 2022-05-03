from tkinter import *
from tkinter import messagebox
import random
import time
import copy


n2_spisok = ()  # конечный список ходов компьютера
ur = 0  # количество предсказываемых компьютером ходов
k_rez = 0
o_rez = 0
pz1_x = -1  # клетка не задана
f_hi = True  # определеяем ход игрока как правда


def level_up():# повышаем количество просчитываемых компльютером ходов
    global ur
    ur += 1
    root.title("Level {}".format(ur))

def level_down():#понижаем количество просчитываемых компльютером ходов
    global ur
    ur -= 1
    root.title("Level {}".format(ur))

def start():# начало игры и условия её начала
    z = 'не верное значение'
    if ur < 0 or ur > 3:
        i = messagebox.askyesno(title=z, message='не верное значение Level!\nНажми "Да" что бы попробовать еще раз.', icon='info')
    if ur >=0 and ur < 4:
        root.destroy()



root = Tk()
root.title("menu")
root.geometry("300x300+300+300")

btn1 = Button(text="start",  # текст кнопки
             background="#555",  # фоновый цвет кнопки
             foreground="#ccc",  # цвет текста
             padx="50",  # отступ от границ до содержимого по горизонтали
             pady="10",  # отступ от границ до содержимого по вертикали
             font="16",  # высота шрифта
             command=start
             )
btn1.pack()

btn2 = Button(text="level up",  # текст кнопки
             background="#555",  # фоновый цвет кнопки
             foreground="#ccc",  # цвет текста
             padx="37",  # отступ от границ до содержимого по горизонтали
             pady="10",  # отступ от границ до содержимого по вертикали
             font="16",  # высота шрифта
             command=level_up
             )
btn2.pack()

btn3 = Button(text="level down",  # текст кнопки
             background="#555",  # фоновый цвет кнопки
             foreground="#ccc",  # цвет текста
             padx="24",  # отступ от границ до содержимого по горизонтали
             pady="10",  # отступ от границ до содержимого по вертикали
             font="16",  # высота шрифта
             command=level_down
             )
btn3.pack()

btn4 = Button(text="quit",  # текст кнопки
              background="#555",  # фоновый цвет кнопки
              foreground="#ccc",  # цвет текста
              padx="54",  # отступ от границ до содержимого по горизонтали
              pady="10",  # отступ от границ до содержимого по вертикали
              font="16",  # высота шрифта
              command=quit
              )
btn4.pack()
root.mainloop()



gl_okno = Tk()  # создаём окно
gl_okno.title("Level {}".format(ur))  # заголовок окна
doska = Canvas(gl_okno, width=800, height=800, bg='#FFFFFF')
doska.pack()

def izobrazheniya_peshek():  #  изображения пешек из папки
    global peshki
    i1 = PhotoImage(file="figuri\\1sha.gif")
    i2 = PhotoImage(file="figuri\\1dam.gif")
    i3 = PhotoImage(file="figuri\\2sha.gif")
    i4 = PhotoImage(file="figuri\\2dam.gif")
    peshki = [0, i1, i2, i3, i4]


def new_game():  # начинаем новую игру
    global pole
    pole = [[0, 3, 0, 3, 0, 3, 0, 3], #расстановка шашек
            [3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]]


def vivod(x_pz_1, y_pz_1, x_pz_2, y_pz_2):  # рисуем игровое поле
    global peshki
    global pole
    global kr_ramka, zel_ramka
    k = 100
    x = 0
    doska.delete('all')
    kr_ramka = doska.create_rectangle(-5, -5, -5, -5, outline="blue", width=5)
    zel_ramka = doska.create_rectangle(-5, -5, -5, -5, outline="yellow", width=5)

    while x < 8 * k:  # рисуем доску(нечетные ряды)(если надо 10х10 то тут до 10 и поле 1000х1000)
        y = 1 * k
        while y < 8 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="black")
            y += 2 * k
        x += 2 * k
    x = 1 * k
    while x < 8 * k:  # рисуем доску(четные ряды)
        y = 0
        while y < 8 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="black")
            y += 2 * k
        x += 2 * k

    for y in range(8):  # рисуем первые позиции пешек
        for x in range(8):
            z = pole[y][x]
            if z:
                if (x_pz_1, y_pz_1) != (x, y):
                    doska.create_image(x * k, y * k, anchor=NW, image=peshki[z])
    # рисуем активную пешку(выделееныую)
    z = pole[y_pz_1][x_pz_1]
    if z:
        doska.create_image(x_pz_1 * k, y_pz_1 * k, anchor=NW, image=peshki[z], tag='ani')
    # для анимации
    kx = 1 if x_pz_1 < x_pz_2 else -1
    ky = 1 if y_pz_1 < y_pz_2 else -1
    for i in range(abs(x_pz_1 - x_pz_2)):  # анимация перемещения пешки(вообще должно былть 33)
        for ii in range(30):
            doska.move('ani', 0.03 * k * kx, 0.03 * k * ky)
            doska.update()  # обновление доски с поставленной пешкой
            time.sleep(0.01)


def soobsenie(s):
    global f_hi
    z = 'Игра завершена'
    if s == 1:
        i = messagebox.askyesno(title=z, message='Вы победили!\nНажми "Да" что бы начать заново.', icon='info')
    if s == 2:
        i = messagebox.askyesno(title=z, message='Вы проиграли!\nНажми "Да" что бы начать заново.', icon='info')
    if s == 3:
        i = messagebox.askyesno(title=z, message='Ходов больше нет.\nНажми "Да" что бы начать заново.', icon='info')
    if i:
        new_game()
        vivod(-1, -1, -1, -1)  # рисуем игровое поле
        f_hi = True  # ход игрока доступен


def pozici_1(event):  # выбор клетки для хода (шаг 1 для хода)
    x, y = (event.x) // 100, (event.y) // 100  # вычисляем координаты клетки
    doska.coords(zel_ramka, x * 100, y * 100, x * 100 + 100, y * 100 + 100)  # рамка в выбранной клетке


def pozici_2(event):  # выбор клетки для хода (шаг для хода №2)
    global pz1_x, pz1_y, pz2_x, pz2_y
    global f_hi
    x, y = (event.x) // 100, (event.y) // 100  # вычисляем координаты клетки
    if pole[y][x] == 1 or pole[y][x] == 2:  # проверяем пешку игрока в выбранной клетке
        doska.coords(kr_ramka, x * 100, y * 100, x * 100 + 100, y * 100 + 100)  # рамка в выбранной клетке
        pz1_x, pz1_y = x, y
    else:
        if pz1_x != -1:  # клетка выбрана
            pz2_x, pz2_y = x, y
            if f_hi:  # проверка ход ли игрока сейчас?
                hod_igroka()
                if not (f_hi):
                    time.sleep(0.5)
                    hod_kompjutera()  # передаём ход компьютеру

            pz1_x = -1  # клетка не выбрана
            doska.coords(kr_ramka, -5, -5, -5, -5)  # рамка вне поля


def hod_kompjutera():  # логика игры за компьютер
    global f_hi
    global n2_spisok
    proverka_hk(1, (), [])
    if n2_spisok:  # проверяем наличие доступных ходов
        kh = len(n2_spisok)  # количество ходов
        th = random.randint(0, kh - 1)  # рандомный ход
        dh = len(n2_spisok[th])  # длина хода
        for h in n2_spisok:  # так надо
            h = h  # и это тоже
        for i in range(dh - 1):            # выполняем ход
            spisok = hod(1, n2_spisok[th][i][0], n2_spisok[th][i][1], n2_spisok[th][1 + i][0], n2_spisok[th][1 + i][1])
        n2_spisok = []  # очищаем список ходов
        f_hi = True  # разрешаем ходить игроку

    # определяем победителя (условия победы)
    s_k, s_i = skan()
    if not (s_i):
        soobsenie(2)
    elif not (s_k):
        soobsenie(1)
    elif f_hi and not (spisok_hi()):
        soobsenie(3)
    elif not (f_hi) and not (spisok_hk()):
        soobsenie(3)


def spisok_hk():  # составляем список ходов компьютера
    spisok = prosmotr_hodov_k1([])  # здесь проверяем обязательные ходы по правилам
    if not (spisok):
        spisok = prosmotr_hodov_k2([])  # здесь проверяем оставшиеся ходы
    return spisok


def proverka_hk(tur, n_spisok, spisok):  # проверка списка ходов
    global pole
    global n2_spisok
    global l_rez, k_rez, o_rez
    if not (spisok):  # если список ходов пустой то 166
        spisok = spisok_hk()  # заполняем

    if spisok: # нахождение лучшего хода в списке
        k_pole = copy.deepcopy(pole)  # копируем поле
        for ((pz1_x, pz1_y), (pz2_x, pz2_y)) in spisok:  # проходим все ходы по списку
            t_spisok = hod(0, pz1_x, pz1_y, pz2_x, pz2_y)
            if t_spisok:  # если существует ещё ход
                proverka_hk(tur, (n_spisok + ((pz1_x, pz1_y),)), t_spisok)
            else:
                proverka_hi(tur, [])
                if tur == 1:
                    t_rez = o_rez / k_rez
                    if not (n2_spisok):  # записыаем если пустой
                        n2_spisok = (n_spisok + ((pz1_x, pz1_y), (pz2_x, pz2_y)),)
                        l_rez = t_rez  # сохряняем наилучший результат
                    else:
                        if t_rez == l_rez:
                            n2_spisok = n2_spisok + (n_spisok + ((pz1_x, pz1_y), (pz2_x, pz2_y)),)
                        if t_rez > l_rez:
                            n2_spisok = ()
                            n2_spisok = (n_spisok + ((pz1_x, pz1_y), (pz2_x, pz2_y)),)
                            l_rez = t_rez  # сохряняем наилучший результат
                    o_rez = 0
                    k_rez = 0

            pole = copy.deepcopy(k_pole)  # возвращаем поле
    else:
        s_k, s_i = skan()  # подсчёт результата хода
        o_rez += (s_k - s_i)
        k_rez += 1


def spisok_hi():  # оцениваем список ходов игрока
    spisok = prosmotr_hodov_i1([])  # проверяем обязательные ходы
    if not (spisok):
        spisok = prosmotr_hodov_i2([])  # проверяем оставшиеся ходы
    return spisok


def proverka_hi(tur, spisok): # проверка списка хдов игрока
    global pole, k_rez, o_rez
    global ur
    if not (spisok):
        spisok = spisok_hi()

    if spisok:  # проверяем наличие доступных ходов
        k_pole = copy.deepcopy(pole)  # копируем поле
        for ((pz1_x, pz1_y), (pz2_x, pz2_y)) in spisok:
            t_spisok = hod(0, pz1_x, pz1_y, pz2_x, pz2_y)
            if t_spisok:  # если существует ещё ход
                proverka_hi(tur, t_spisok)
            else:
                if tur < ur:
                    proverka_hk(tur + 1, (), [])
                else:
                    s_k, s_i = skan()  # подсчёт результата хода
                    o_rez += (s_k - s_i)
                    k_rez += 1

            pole = copy.deepcopy(k_pole)  # возвращаем поле
    else:  # если доступных ходов нет
        s_k, s_i = skan()  # подсчёт результата хода
        o_rez += (s_k - s_i)
        k_rez += 1


def skan():  # подсчёт пешек на поле
    global pole
    s_i = 0
    s_k = 0
    for i in range(8):
        for ii in pole[i]:
            if ii == 1: s_i += 1
            if ii == 2: s_i += 3
            if ii == 3: s_k += 1
            if ii == 4: s_k += 3
    return s_k, s_i


def hod_igroka():
    global pz1_x, pz1_y, pz2_x, pz2_y
    global f_hi
    f_hi = False  # считаем ход игрока выполненным
    spisok = spisok_hi()
    if spisok:
        if ((pz1_x, pz1_y), (pz2_x, pz2_y)) in spisok:  # проверяем ход на соответствие правилам игры
            t_spisok = hod(1, pz1_x, pz1_y, pz2_x, pz2_y)  # если всё хорошо, делаем ход
            if t_spisok:  # если есть ещё ход той же пешкой
                f_hi = True  # считаем ход игрока невыполненным
        else:
            f_hi = True  # считаем ход игрока невыполненным
    doska.update()  # !!!обновление


def hod(f, pz1_x, pz1_y, pz2_x, pz2_y):
    global pole
    if f: vivod(pz1_x, pz1_y, pz2_x, pz2_y)  # рисуем игровое поле
    # превращение
    if pz2_y == 0 and pole[pz1_y][pz1_x] == 1:
        pole[pz1_y][pz1_x] = 2
    # превращение
    if pz2_y == 7 and pole[pz1_y][pz1_x] == 3:
        pole[pz1_y][pz1_x] = 4
    # делаем ход
    pole[pz2_y][pz2_x] = pole[pz1_y][pz1_x]
    pole[pz1_y][pz1_x] = 0

    # рубим пешку игрока
    kx = ky = 1
    if pz1_x < pz2_x: kx = -1
    if pz1_y < pz2_y: ky = -1
    x_poz, y_poz = pz2_x, pz2_y
    while (pz1_x != x_poz) or (pz1_y != y_poz):
        x_poz += kx
        y_poz += ky
        if pole[y_poz][x_poz] != 0:
            pole[y_poz][x_poz] = 0
            if f: vivod(-1, -1, -1, -1)  # рисуем игровое поле
            # проверяем ход той же пешкой...
            if pole[pz2_y][pz2_x] == 3 or pole[pz2_y][pz2_x] == 4:  # ...компьютера
                return prosmotr_hodov_k1p([], pz2_x, pz2_y)  # возвращаем список доступных ходов
            elif pole[pz2_y][pz2_x] == 1 or pole[pz2_y][pz2_x] == 2:  # ...игрока
                return prosmotr_hodov_i1p([], pz2_x, pz2_y)  # возвращаем список доступных ходов
    if f: vivod(pz1_x, pz1_y, pz2_x, pz2_y)  # рисуем игровое поле


def prosmotr_hodov_k1(spisok):  # проверка наличия обязательных ходов
    for y in range(8):  # сканируем всё поле
        for x in range(8):
            spisok = prosmotr_hodov_k1p(spisok, x, y)
    return spisok


def prosmotr_hodov_k1p(spisok, x, y):
    if pole[y][x] == 3:  # пешка
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            if 0 <= y + iy + iy <= 7 and 0 <= x + ix + ix <= 7:
                if pole[y + iy][x + ix] == 1 or pole[y + iy][x + ix] == 2:
                    if pole[y + iy + iy][x + ix + ix] == 0:
                        spisok.append(((x, y), (x + ix + ix, y + iy + iy)))  # запись хода в конец списка
    if pole[y][x] == 4:  # пешка с короной
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            osh = 0  # определение правильности хода
            for i in range(1, 8):
                if 0 <= y + iy * i <= 7 and 0 <= x + ix * i <= 7:
                    if osh == 1:
                        spisok.append(((x, y), (x + ix * i, y + iy * i)))  # запись хода в конец списка
                    if pole[y + iy * i][x + ix * i] == 1 or pole[y + iy * i][x + ix * i] == 2:
                        osh += 1
                    if pole[y + iy * i][x + ix * i] == 3 or pole[y + iy * i][x + ix * i] == 4 or osh == 2:
                        if osh > 0: spisok.pop()  # удаление хода из списка
                        break
    return spisok


def prosmotr_hodov_k2(spisok):  # проверка наличия остальных ходов
    for y in range(8):  # сканируем всё поле
        for x in range(8):
            if pole[y][x] == 3:  # пешка
                for ix, iy in (-1, 1), (1, 1):
                    if 0 <= y + iy <= 7 and 0 <= x + ix <= 7:
                        if pole[y + iy][x + ix] == 0:
                            spisok.append(((x, y), (x + ix, y + iy)))  # запись хода в конец списка
                        if pole[y + iy][x + ix] == 1 or pole[y + iy][x + ix] == 2:
                            if 0 <= y + iy * 2 <= 7 and 0 <= x + ix * 2 <= 7:
                                if pole[y + iy * 2][x + ix * 2] == 0:
                                    spisok.append(((x, y), (
                                    x + ix * 2, y + iy * 2)))  # запись хода в конец списка
            if pole[y][x] == 4:  # пешка с короной
                for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                    osh = 0  # определение правильности хода
                    for i in range(1, 8):
                        if 0 <= y + iy * i <= 7 and 0 <= x + ix * i <= 7:
                            if pole[y + iy * i][x + ix * i] == 0:
                                spisok.append(((x, y), (x + ix * i, y + iy * i)))  # запись хода в конец списка
                            if pole[y + iy * i][x + ix * i] == 1 or pole[y + iy * i][x + ix * i] == 2:
                                osh += 1
                            if pole[y + iy * i][x + ix * i] == 3 or pole[y + iy * i][x + ix * i] == 4 or osh == 2:
                                break
    return spisok


def prosmotr_hodov_i1(spisok):  # проверка наличия обязательных ходов
    spisok = []  # список ходов
    for y in range(8):  # сканируем всё поле
        for x in range(8):
            spisok = prosmotr_hodov_i1p(spisok, x, y)
    return spisok


def prosmotr_hodov_i1p(spisok, x, y):
    if pole[y][x] == 1:  # пешка
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            if 0 <= y + iy + iy <= 7 and 0 <= x + ix + ix <= 7:
                if pole[y + iy][x + ix] == 3 or pole[y + iy][x + ix] == 4:
                    if pole[y + iy + iy][x + ix + ix] == 0:
                        spisok.append(((x, y), (x + ix + ix, y + iy + iy)))  # запись хода в конец списка
    if pole[y][x] == 2:  # дамка
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            osh = 0  # определение правильности хода
            for i in range(1, 8):
                if 0 <= y + iy * i <= 7 and 0 <= x + ix * i <= 7:
                    if osh == 1:
                        spisok.append(((x, y), (x + ix * i, y + iy * i)))  # запись хода в конец списка
                    if pole[y + iy * i][x + ix * i] == 3 or pole[y + iy * i][x + ix * i] == 4:
                        osh += 1
                    if pole[y + iy * i][x + ix * i] == 1 or pole[y + iy * i][x + ix * i] == 2 or osh == 2:
                        if osh > 0: spisok.pop()  # удаление хода из списка
                        break
    return spisok


def prosmotr_hodov_i2(spisok):  # проверка наличия остальных ходов
    for y in range(8):  # сканируем всё поле
        for x in range(8):
            if pole[y][x] == 1:  # пешка
                for ix, iy in (-1, -1), (1, -1):
                    if 0 <= y + iy <= 7 and 0 <= x + ix <= 7:
                        if pole[y + iy][x + ix] == 0:
                            spisok.append(((x, y), (x + ix, y + iy)))  # запись хода в конец списка
                        if pole[y + iy][x + ix] == 3 or pole[y + iy][x + ix] == 4:
                            if 0 <= y + iy * 2 <= 7 and 0 <= x + ix * 2 <= 7:
                                if pole[y + iy * 2][x + ix * 2] == 0:
                                    spisok.append(((x, y), (
                                    x + ix * 2, y + iy * 2)))  # запись хода в конец списка
            if pole[y][x] == 2:  # пешка с короной
                for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                    osh = 0  # определение правильности хода
                    for i in range(1, 8):
                        if 0 <= y + iy * i <= 7 and 0 <= x + ix * i <= 7:
                            if pole[y + iy * i][x + ix * i] == 0:
                                spisok.append(((x, y), (x + ix * i, y + iy * i)))  # запись хода в конец списка
                            if pole[y + iy * i][x + ix * i] == 3 or pole[y + iy * i][x + ix * i] == 4:
                                osh += 1
                            if pole[y + iy * i][x + ix * i] == 1 or pole[y + iy * i][x + ix * i] == 2 or osh == 2:
                                break
    return spisok


izobrazheniya_peshek()  # здесь загружаем изображения пешек
new_game()  # начинаем новую игру
vivod(-1, -1, -1, -1)  # рисуем игровое поле
doska.bind("<Motion>", pozici_1)  # движение мышки по полю
doska.bind("<Button-1>", pozici_2)  # нажатие левой кнопки
mainloop()


