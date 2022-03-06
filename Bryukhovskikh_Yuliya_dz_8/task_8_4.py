from functools import wraps


def val_checker(callback):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args):
            if args:
                for arg in args:
                    if not callback(arg):
                        raise ValueError(f'Аргумент {arg} не прошёл валидацию')
            return func(*args)
        return wrapper
    return my_decorator


def positive(x: int) -> bool:
    """
    Проверяет, положителен ли аргумент
    """
    return x >= 0 if isinstance(x, int) else False


@val_checker(positive)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
