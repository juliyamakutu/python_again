from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix) - 1 ):
            if len(matrix[i]) != len(matrix[i+1]):
                raise ValueError('fail initialization matrix')
        self.matrix = matrix

    def __str__(self):
        msg =''
        for line in self.matrix:
            msg += '| ' + ' '.join([str(el) for el in line]) + ' |\n'
        return msg+'\n'

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result_line = []
            for j in range(len(self.matrix[i])):
                result_line.append(self.matrix[i][j]+other.matrix[i][j])
            result.append(result_line)
        return Matrix(result)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """