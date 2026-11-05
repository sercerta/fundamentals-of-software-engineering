# A2. Проверка надежности введенного пароля.

import string

# Получаем пароль от пользователя
password = input()

# Собираем все допустимые символы: латинские буквы, цифры и * - #
allowed = (
    string.ascii_uppercase
    + string.ascii_lowercase
    + string.digits
    + "*-#"
)

# Проверяем каждое требование и выводим все обнаруженные ошибки
has_errors = False

if len(password) != 8:
    print("Длина пароля не равна 8")
    has_errors = True

if password == password.lower():
    print("В пароле отсутствуют заглавные буквы")
    has_errors = True

if password == password.upper():
    print("В пароле отсутствуют строчные буквы")
    has_errors = True

if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры")
    has_errors = True

if not any(symbol in "*-#" for symbol in password):
    print("В пароле отсутствуют специальные символы")
    has_errors = True

if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")
    has_errors = True

# Если ошибок нет, пароль соответствует всем требованиям
if not has_errors:
    print("Надежный пароль")
