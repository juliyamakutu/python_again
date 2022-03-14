from model import ColorType, PrinterType, Printer, Scaner, Copier, Storage
from exceptions import SizeExceeded, WrongItem, NumberDuplicate, NumberNotExists


if __name__ == '__main__':
    # Созадаём два склада
    storage = Storage('Склад')
    office = Storage('Офис')
    # Создаём технику
    hp_printer = Printer(
        size=10,
        price=45000,
        brand='HP',
        number=100,
        page_per_min=50,
        type=PrinterType.laser,
        color_type=ColorType.black_white
    )
    big_printer = Printer(
        size=100,
        price=150000,
        brand='Xerox',
        number=13,
        page_per_min=150,
        type=PrinterType.laser,
        color_type=ColorType.color,
    )
    scaner = Scaner(
        size=5,
        price=15000,
        brand='Canon',
        number=42,
        feeder=True,
    )
    copier = Copier(
        size=15,
        price=20000,
        brand='Xerox',
        number=66,
        color_type=ColorType.black_white,
        page_per_min=15,
        feeder=True,
    )
    kyosera_printer = Printer(
        size=50,
        price=90000,
        brand='Kyocera',
        number=15,
        page_per_min=50,
        type=PrinterType.laser,
        color_type=ColorType.color
    )
    dupe_copier = Copier(
        size=5,
        price=10000,
        brand='Canon',
        number=13,
        color_type=ColorType.black_white,
        page_per_min=5,
        feeder=False,
    )

    # добавляем техинку на склад
    print("Добавляем технику на склад")
    storage.add(hp_printer)
    storage.add(kyosera_printer)
    storage.add(copier)
    storage.add(scaner)
    # пробуем добавить слишком большой принтер
    try:
        storage.add(big_printer)
    except SizeExceeded as err:
        print(err)
    # пробуем добавить технику с дубликатом инвинтарного номера
    try:
        storage.add(dupe_copier)
    except NumberDuplicate as err:
        print(err)
    # пробуем добавить неверный тип объекта
    try:
        storage.add('printer')
    except WrongItem as err:
        print(err)
    # выводим содержимое складов
    print(storage)
    print(office)
    print("Перемещаем технику")
    # пробуем переместить технику с несуществующим номером
    try:
        storage.move(666, office)
    except NumberNotExists as err:
        print(err)
    # переместим в офис минимальный набор техники
    storage.move(100, office)
    storage.move(42, office)
    storage.move(66, office)
    # выведем содержимое складов
    print(storage)
    print(office)