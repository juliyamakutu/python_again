from abc import ABC
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

from exceptions import WrongItem, SizeExceeded, NumberDuplicate, NumberNotExists
from settings import DEFAILT_STORAGE_CAPACITY


class PrinterType(Enum):
    laser = 'laser'
    jet = 'jet'
    sublimation = 'sublimation'


class ColorType(Enum):
    black_white = 'black and white'
    color = 'color'


@dataclass
class Equipment(ABC):
    size: int
    price: float
    brand: str
    number: int

    def __str__(self):
        return f"{self.__class__.__name__} {self.brand}"


@dataclass
class Printer(Equipment):
    page_per_min: int
    type: PrinterType
    color_type: ColorType


@dataclass
class Scaner(Equipment):
    feeder: bool


@dataclass
class Copier(Equipment):
    feeder: bool
    page_per_min: int
    color_type: ColorType


class Storage:
    _capacity = DEFAILT_STORAGE_CAPACITY
    _equipments = Dict[int, Equipment]

    def __init__(self, name: str):
        self._equipments = {}
        self.name = name

    def add(self, item: Equipment):
        """Добавляет оборудование на склад"""
        if not isinstance(item, Equipment):
            raise WrongItem
        if self.number_exists(item.number):
            raise NumberDuplicate
        if self.used + item.size > self._capacity:
            raise SizeExceeded
        self._equipments[item.number] = item

    def __remove(self, number: int):
        if not self.number_exists(number):
            raise NumberNotExists
        del self._equipments[number]

    def move(self, number, storage: 'Storage'):
        """Перемещает оборудование на другой склад"""
        if not self.number_exists(number):
            raise NumberNotExists
        item = self._equipments[number]
        storage.add(item)
        self.__remove(number)

    @property
    def used(self) -> int:
        """Возвращает использованное место"""
        return sum([item.size for item in self._equipments.values()])

    def number_exists(self, number: int) -> bool:
        """Проверяет наличие инвентарного номер на складе"""
        return number in self._equipments.keys()

    def __str__(self):
        """Выводит содержимое склада"""
        msg = f'Оборудование в "{self.name}:"\n'
        for el in self._equipments.values():
            msg += f'\t{el.number}: {el}\n'
        return msg

    def __getitem__(self, number: int) -> Equipment:
        if not self.number_exists(number):
            raise NumberNotExists
        return self._equipments[number]