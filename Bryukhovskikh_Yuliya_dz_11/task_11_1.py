import re


class Date:
    def __init__(self, date: str):
        # валидирвем данные
        self.validate(date)
        day, month, year = date.split('-')
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def validate(date: str) -> None:
        validator = re.compile("^(?P<day>[0-9]{1,2})-(?P<month>[0-9]{1,2})-(?P<year>[0-9]{1,4})$")
        result = validator.match(date)
        if not result:
            raise ValueError('Невернй формат даты')
        result_dict = result.groupdict()
        if int(result_dict['day']) < 1 or int(result_dict['day']) > 31:
            raise ValueError('Неверный формат дня')
        if int(result_dict['month']) < 1 or int(result_dict['month']) > 12:
            raise ValueError('Неверный формат месяца')

    @classmethod
    def as_number(cls, date: str) -> (int, int, int):
        instance = cls(date)
        return int(instance.day), int(instance.month), int(instance.year)

    def __str__(self):
        return f'{self.day.zfill(2)}.{self.month.zfill(2)}.{self.year.zfill(2)}'


if __name__ == '__main__':
    # проверка метода as_number
    print(Date.as_number('12-12-2021'))
    # проверка констурктора класса
    print(Date('1-1-1'))
    # проверка валидатора
    Date.validate('15-13-2011')