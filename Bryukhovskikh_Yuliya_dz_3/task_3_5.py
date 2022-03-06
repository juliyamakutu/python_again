from random import randint


def get_jokes(count: int,  reuse: bool = True) -> list:
    """
    Возвращает список шуток в количестве count
    :param count: колличество шуток
    :param reuse: омжет ли одно и тоже слово повторяться в разных шутках
    :return: список шуток
    """

    # задаём списки слов
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    # если count больше длины списка и нельзя использовать слова повторно, то ограничим count
    if not reuse and count > len(nouns):
        count = len(nouns)

    list_out = []
    for _ in range(count):
        # берём случайные элементы списков
        # если можно использовать слова повторно
        if reuse:
            a = nouns[randint(0, len(nouns) - 1)]
            b = adverbs[randint(0, len(adverbs) - 1)]
            c = adjectives[randint(0, len(adjectives) - 1)]
        # если нельзя использовать слова повторно
        else:
            a = nouns.pop(randint(0, len(nouns) - 1))
            b = adverbs.pop(randint(0, len(adverbs) - 1))
            c = adjectives.pop(randint(0, len(adjectives) - 1))
        # формируем шутку из трёх слов
        list_out.append(f"{a} {b} {c}")

    return list_out


# Проверяем работу функции на тестовых данных
print(get_jokes(2))
print(get_jokes(10))
print(get_jokes(0))
print(get_jokes(reuse=False, count=10))
print(get_jokes(reuse=False, count=8))
print(get_jokes(reuse=False, count=3))