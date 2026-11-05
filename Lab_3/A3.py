# A3. Расчет объема использованного газа и суммы оплаты.

from decimal import Decimal, ROUND_HALF_UP

# Ввод показаний счетчика за предыдущий и текущий месяцы
previous = int(input())
current = int(input())

# Счетчик имеет значения от 0 до 9999 и после 9999 обнуляется
if current >= previous:
    used = current - previous
else:
    used = (10000 - previous) + current

# Расчет оплаты по последовательным тарифным диапазонам.
# Decimal позволяет точно работать с десятичными тарифами.
if used <= 300:
    payment = Decimal("21.00")
elif used <= 600:
    payment = Decimal("21.00") + Decimal(used - 300) * Decimal("0.06")
elif used <= 800:
    payment = (
        Decimal("21.00")
        + Decimal(300) * Decimal("0.06")
        + Decimal(used - 600) * Decimal("0.04")
    )
else:
    payment = (
        Decimal("21.00")
        + Decimal(300) * Decimal("0.06")
        + Decimal(200) * Decimal("0.04")
        + Decimal(used - 800) * Decimal("0.025")
    )

# Средняя цена кубометра; при нулевом расходе деления на ноль нет
if used == 0:
    average_price = Decimal("0.00")
else:
    average_price = payment / Decimal(used)

# Округляем денежные значения до двух знаков по обычному правилу
payment = payment.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
average_price = average_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# Выводим результаты в виде таблицы
print(f"{'Предыдущее':>12} {'Текущее':>12} {'Использовано':>14} {'К оплате':>12} {'Ср. цена m^3':>14}")
print(f"{previous:12d} {current:12d} {used:14d} {payment:12.2f} {average_price:14.2f}")
