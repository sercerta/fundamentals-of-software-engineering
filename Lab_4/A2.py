# A2. Рисование фигур с помощью вложенных циклов.
def draw_rectangle(rows, columns, ch):
    for _ in range(rows):
        for _ in range(columns):
            print(ch, end="")
        print()


def draw_triangle(rows, ch):
    for i in range(1, rows + 1):
        for _ in range(i):
            print(ch, end="")
        print()


def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Введите положительное число.")
        except ValueError:
            print("Введите целое число.")

n = read_positive_int("Введите количество строк n: ")
m = read_positive_int("Введите количество столбцов m: ")
symbol = input("Введите символ для рисования: ")
symbol = symbol[0] if symbol else "#"
print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
draw_rectangle(n, m, symbol)
print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
draw_triangle(n, symbol)
print(f"\nРАМКА {n}x{m}:")
draw_frame(n, m, symbol)
