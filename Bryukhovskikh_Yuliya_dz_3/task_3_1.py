from typing import Optional


# создаём англо-русский словарь для перевода числительных от 0 до 10 как константу
DICT = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "seven": "семь",
    "six": "шесть",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}


def num_translate(value: str) -> Optional[str]:
    """переводит числительное от 0 до 10 с английского на русский """
    # получаем перевод из словаря, если такого ключа нет get вернёт None
    str_out = DICT.get(value)
    return str_out


# Проверяем работу функции на тестовых данных
print('Перевод "one":', num_translate('one'))
print('Перевод "eight":', num_translate('eight'))
print('Перевод "seven:"', num_translate('seven'))
print('Перевод "eleven":', num_translate('eleven'))