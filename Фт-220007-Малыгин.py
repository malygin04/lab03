# Функция для определения цвета поля
def check_color(k, l):
    if (k + l) % 2 == 0:
        return "белый"
    else:
        return "чёрный"

# Функция для проверки угрозы фигуры полю
def check_threat(figure, k , l, m, n):
    if figure == "ферзь" or figure == "ладья":
        if k == m or l == n:
            return True
    if figure == "ферзь" or figure == "слон":
        if abs(k - m) == abs(l - n):
            return True
    if figure == "конь":
        if (abs(k - m) == 2 and abs(l - n) == 1) or (abs(k - m) == 1 and abs(l - n) == 2):
            return True
        return False

# Функция для проверки возможности хода фигуры на поле
def check_move(figure, k, l, m, n):
    if figure == "ладья":
        if k == m or l == n:
            return True
    if figure == "ферзь":
        if k == m or l == n or abs(k - m) == abs(l - n):
            return True
    if figure == "слон":
        if abs(k - m) == abs(l - n):
            return True
        return False

# Функция для определения возможности попадания на поле за два хода
def check_move_in_two_steps(figure,k, l, m, n):
    if figure == "слон":
        for i in range(1, 9):
            for j in range(1, 9):
                if abs(k - i) == abs(l - j) and abs(i - m) == abs(j - n):
                    return True
        return False
    else:
        return False

# Функция для определения клетки, в которую фигура сможет попасть после двух ходов
def get_next_move(figure, k, l, m, n):
    for i in range(1, 9):
        for j in range(1, 9):
            if check_move(figure, k, l, i, j) and check_move(figure, i, j, m, n):
                return i, j
    return None

# Основная часть программы
print("Введите координаты первого поля (k, l):")
k = int(input())
l = int(input())
print("Введите координаты второго поля (m, n):")
m = int(input())
n = int(input())

# Условие для данных полей
while k >= 9 or l >= 9 or m >= 9 or n >= 9:
        print("Введенные данные должны быть числами меньше или равными 8.")
        k = int(input("Введите номер вертикали для первого поля: "))
        l = int(input("Введите номер горизонтали для первого поля: "))
        m = int(input("Введите номер вертикали для второго поля: "))
        n = int(input("Введите номер горизонтали для второго поля: "))

# Проверка цвета полей
color1 = check_color(k, l)
color2 = check_color(m, n)
print("Цвет первого поля:", color1)
print("Цвет второго поля:", color2)

if color1 == color2:
    print("Поля (k, l) и (m, n) имеют одинаковый цвет.")
else:
    print("Поля (k, l) и (m, n) имеют разный цвет.")

print("Введите фигуру (ферзь, ладья, слон или конь):")
figure = input()

# Проверка угрозы фигуры полю
if check_threat(figure, k, l, m, n):
    print("Фигура угрожает полю (m, n).")
else:
    print("Фигура не угрожает полю (m, n).")

# Проверка возможности попадания на поле
if check_move(figure, k, l, m, n):
    print("Фигура", figure, "может попасть на поле (", m, ",", n, ") одним ходом.")
elif check_move_in_two_steps(figure, k, l, m, n):
    next_move = get_next_move(figure, k, l, m, n)
    if next_move:
        print("Фигура", figure, "может попасть на поле (", m, ",", n, ") за два хода.")
        print("Следующий ход: (", next_move[0], ",", next_move[1], ")")
    else:
        print("Фигура", figure, "может попасть на поле (", m, ",", n, ") за два хода.")
else:
    print("Фигура", figure, "не может попасть на поле (", m, ",", n, ") за два хода.")




