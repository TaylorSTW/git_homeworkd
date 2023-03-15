"""Функция, делающая заглавные буквы вслове
"""
def str_function():
    lower_line = input("Введите слово")
    for letter in lower_line:
        letter = lower_line.upper()
    return letter

print(str_function())
