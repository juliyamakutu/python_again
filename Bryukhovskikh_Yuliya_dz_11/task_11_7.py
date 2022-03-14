class Complex:
    real: float
    imaginarius: float

    def __init__(self, real: float, imaginarius: float):
        self.real = real
        self.imaginarius = imaginarius

    def __str__(self):
        return f'{self.real}+{self.imaginarius}i'

    def __repr__(self):
        return f'{self.real}+{self.imaginarius}i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(
                real=self.real+other.real,
                imaginarius=self.imaginarius+self.imaginarius
            )
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(
                real=self.real + other,
                imaginarius=self.imaginarius
            )
        else:
            raise ValueError('Можно сложить только с комлесным, целым или числом с плавающей точкой')

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(
                real=self.real * other.real,
                imaginarius=self.imaginarius * other.imaginarius
            )
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(
                real=self.real * other,
                imaginarius=self.imaginarius
            )
        else:
            raise ValueError('Можно сложить только с комлесным, целым или числом с плавающей точкой')


if __name__ == '__main__':
    complex_1 = Complex(5, 7)
    complex_2 = Complex(6, 10)
    print(f'{complex_1=}, {complex_2=}')
    print(f'complex_1 * complex_2 = {complex_1 * complex_2}')
    print(f'complex_1 + complex_2 = {complex_1 + complex_2}')
    print(f'complex_1 * 3,14 = ', complex_1 * 3.14)
    print(f'complex_2 + 11 = ', complex_2 + 11)