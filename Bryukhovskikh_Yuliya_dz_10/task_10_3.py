from functools import wraps


def cell_validator(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, Cell):
                raise TypeError('действие допустимо только для экземпляров того же класса')
        return func(*args)
    return wrapper


class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def make_order(self, number: int) -> str:
        result = ''
        for i in range(1, self.cells + 1):
            result += '*'
            if i % number == 0:
                result += '\n'
        return result

    @cell_validator
    def __add__(self, other):
        return Cell(self.cells + other.cells)

    @cell_validator
    def __sub__(self, other):
        if (result := self.cells - other.cells) < 0:
            raise ValueError('недопустимая операция')
        return Cell(result)

    @cell_validator
    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    @cell_validator
    def __truediv__(self, other):
        return self.__floordiv__(other)

    @cell_validator
    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса
