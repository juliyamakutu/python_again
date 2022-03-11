import os
import sys

from collections import defaultdict
from typing import Tuple
from pprint import pprint


def frontier(x: int) -> Tuple[int, int]:
    exponent = len(str(x))
    return 10 ** exponent


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <folder>')
    statistic = defaultdict(int)
    folder = os.path.abspath(sys.argv[1])
    if not os.path.exists(folder):
        raise FileNotFoundError('Неправильный путь')
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_size = os.stat(os.path.join(path, file)).st_size
            if file_size == 0:
                statistic[file_size] += 1
            else:
                statistic[frontier(file_size)] += 1
    pprint(dict(statistic))
