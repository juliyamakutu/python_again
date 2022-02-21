from typing import Generator


def odd_nums(number: int) -> Generator[int, None, None]:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно) без yield"""
    return (i for i in range(1, n+1, 2))


n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
