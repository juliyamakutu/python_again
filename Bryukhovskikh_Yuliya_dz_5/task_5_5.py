from collections import defaultdict
from typing import Generator, Any


def get_uniq_numbers(src: list) -> Generator[Any, None, None]:
    """генератор возвращает элементы списка не имеющие повторений
    :param src: входной список
    :returns: генератор значений не имеющих повторений
    """
    count = defaultdict(int)
    # считаем элементы списка
    for el in src:
        count[el] += 1
    # возвращает элемент встречающийся один раз
    for key, value in count.items():
        if value == 1:
            yield key

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))