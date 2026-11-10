# A4. Проверка номера банковской карты и определение ее типа.

def isValidNumber(string):
    """Проверяет, что номер состоит только из цифр и имеет допустимую длину."""
    return string.isdigit() and len(string) in (13, 15, 16)


def getCheckSum(string):
    """Вычисляет контрольную сумму номера карты по алгоритму Луна."""
    checkSum = 0

    for i in range(len(string) - 2, -1, -2):
        digit = int(string[i]) * 2

        if digit > 9:
            digit = digit - 9

        checkSum += digit

    for i in range(len(string) - 1, -1, -2):
        checkSum += int(string[i])

    return checkSum


def getCardType(string):
    """Возвращает тип карты или Invalid, если префикс и длина не подходят."""
    if len(string) == 13 or len(string) == 16:
        if string.startswith("4"):
            return "Visa"

    if len(string) == 15:
        if string.startswith(("34", "37")):
            return "American Express"

    if len(string) == 16:
        if string.startswith(("51", "52", "53", "54", "55")):
            return "Master Card"

    return "Invalid"


cardNumber = input("Введите номер банковской карты: ").strip()

if isValidNumber(cardNumber):
    cardType = getCardType(cardNumber)

    if cardType != "Invalid" and getCheckSum(cardNumber) % 10 == 0:
        print(cardType)
    else:
        print("Invalid")
else:
    print("Invalid")
