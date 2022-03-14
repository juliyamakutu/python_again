class MyZeroError(Exception):
    def __init__(self, text):
        self.text = text


try:
    dividend = int(input('Введите делимое: '))
    divider = int(input('Введите делитель: '))
    if divider == 0:
        raise MyZeroError('Деление на ноль!')
    print('Частное: ', dividend/divider)
except ValueError:
    print('Надо ввести числа')
except MyZeroError as err:
    print('Произошал ошибка:', err)