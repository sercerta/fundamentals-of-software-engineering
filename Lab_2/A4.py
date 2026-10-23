# A4. Вывести наибольшее из двух целых чисел без ветвлений и циклов.
a = int(input())
b = int(input())

result = [a, b][a <= b]
print(result)
