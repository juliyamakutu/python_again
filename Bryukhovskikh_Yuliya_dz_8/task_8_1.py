import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?P<username>[\w.-]+)@(?P<domain>[A-Za-z0-9-]{2,}\.[A-Za-z]{2,})')

    result = RE_MAIL.match(email)

    if not result:
        raise ValueError('Некорректный адрес электронной почты')

    return result.groupdict()


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))