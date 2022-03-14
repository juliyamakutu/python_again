from typing import Optional


class StorageException(Exception):
    _default_text: str = 'Неизвестная ошибка склада'

    def __init__(self, text: Optional[str] = None, *args, **kwargs):
        msg = text if text else self._default_text
        super().__init__(msg, *args, **kwargs)


class WrongItem(StorageException):
    _default_text: str = 'Объект не является оборудованием'


class SizeExceeded(StorageException):
    _default_text: str = 'Превышена ёмкость склада'


class NumberDuplicate(StorageException):
    _default_text: str = 'Такой инвентарый номер уже есть'


class NumberNotExists(StorageException):
    _default_text: str = 'Нет такого инвентаорного номера'

