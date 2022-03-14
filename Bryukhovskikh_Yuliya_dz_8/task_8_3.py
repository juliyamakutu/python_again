from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__}(', end='')
        print(', '.join([f'{arg}: {type(arg)}' for arg in args]), end='')
        print(', '.join([f'{key}={val}: {type(val)}' for key, val in kwargs.items()]), end='')
        print(')')
        return func(*args, **kwargs)
    return wrapper


@type_logger
def calc_cube(x: int) -> int:
    """
    Функция возвращающая кубы
    :param x: числа возводимые в куб
    :return: выводит куб числа
    """
    return x ** 3


@type_logger
def degree(base: int, indicator: int) -> int:
    """
    Функция возвращает base в степени indicator
    :param base: основание степени
    :param indicator: показатель степени
    :return: результат возведения в степень
    """
    return base ** indicator


# проверяем работу декоратора
print(calc_cube(5))
print(calc_cube(x=5))
print(degree(5,2))
print(degree(3, indicator=2))
print(degree(base=5, indicator=4))
# проверяем маскировку декоратора
print(calc_cube.__name__)
print(calc_cube.__doc__)
print(help(calc_cube))
print(degree.__name__)
print(degree.__doc__)
print(help(degree))