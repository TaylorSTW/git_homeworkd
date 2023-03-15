def str_function():
    """
    Функция, которая делает все буквы заглавными

    """
    lower_line = input("Введите слово ")
    for letter in lower_line:
        letter = lower_line.upper()
    return letter


def new_str():
    """
    Функия, кторая делает первую букву заглавной

    """
    letter = input('Введите слово ').capitalize()
    return letter


print(new_str())