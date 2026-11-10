# A3. Анализ последовательности доставленных и потерянных пакетов.
while True:
    packets = input("Введите последовательность из 0 и 1 (не менее 5 символов): ")
    if len(packets) < 5:
        print("Ошибка: длина строки должна быть не меньше 5.")
        continue
    if not all(char in "01" for char in packets):
        print("Ошибка: используйте только символы 0 и 1.")
        continue
    break

total_packets = len(packets)
lost_packets = packets.count("0")
loss_percent = lost_packets / total_packets * 100
longest_streak = 0
current_streak = 0
for packet in packets:
    if packet == "0":
        current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    else:
        current_streak = 0

if loss_percent <= 1:
    quality = "отличное"
elif loss_percent <= 5:
    quality = "хорошее"
elif loss_percent <= 10:
    quality = "удовлетворительное"
elif loss_percent <= 20:
    quality = "плохое"
else:
    quality = "критическое состояние сети"

print("\nРЕЗУЛЬТАТЫ АНАЛИЗА:")
print(f"Общее количество пакетов: {total_packets}")
print(f"Количество потерянных пакетов: {lost_packets}")
print(f"Длина самой длинной последовательности потерянных пакетов: {longest_streak}")
print(f"Процент потерь: {loss_percent:.1f}%")
print(f"Качество связи: {quality}")
