# A6. Перевести N секунд с начала суток в формат h:mm:ss.
n = int(input())

hours = (n // 3600) % 24
minutes = (n % 3600) // 60
seconds = n % 60

print("{}:{:02d}:{:02d}".format(hours, minutes, seconds))
