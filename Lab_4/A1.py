# A1. Тренажёр для изучения таблицы умножения.
import random
import time

while True:
    try:
        n = int(input("Введите количество примеров: "))
        if n > 0:
            break
        print("Количество примеров должно быть положительным.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

correct = 0
total_time = 0.0
for i in range(1, n + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    print(f"Вопрос {i}/{n}")
    start_time = time.time()
    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    elapsed = time.time() - start_time
    total_time += elapsed
    if answer == a * b:
        correct += 1
        print(f"Верно! (Время: {elapsed:.1f} сек)")
    else:
        print(f"Неверно! Правильно: {a * b} (Время: {elapsed:.1f} сек)")

print("=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time / n:.1f} сек")
print(f"Правильных ответов: {correct}/{n}")
print(f"Процент правильных: {correct / n * 100:.1f}%")
