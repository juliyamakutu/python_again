from datetime import datetime, date
import requests

# адрес источника данных по курсам валют
CURRENCY_SRC = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates_adv(code: str):
    """
        Функция возвращает курс валют на текущую дату
        :param currency: трёхбуквенный код валюты
        :return: кортеж из курса валюты и дата ответа сервера
        """
    # выполняем запрос
    result = requests.get(CURRENCY_SRC)
    # получаем дату
    cur_datetime = datetime.strptime(result.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    # получаем ответ в текстовом виде
    cur_xml = result.text

    # находим начало блока с валютой
    cur_start = cur_xml.find(f'<CharCode>{code.upper()}</CharCode>')
    # если такой блок не найден - возвращаем None
    if cur_start == -1:
        return None, None
    # находоим начало блока со значением курса и сдвигаем на длину тега
    cur_start = cur_xml.find('<Value>', cur_start) + 7
    # находим конец блока со значением валюты
    cur_end = cur_xml.find('</Value>', cur_start)
    # возвращем значение валюты и дату
    return float(cur_xml[cur_start:cur_end].replace(',', '.')), cur_datetime.date()

currencies = ['USD', 'BGN', 'CAD', 'EUR']

for currency in currencies:
    kurs, date_value = currency_rates_adv(currency)

    empty = bool(not kurs and not date_value)
    if not empty and not isinstance(kurs, float):
        raise TypeError("Неверный тип данных у курса")
    if not empty and not isinstance(date_value, date):
        raise TypeError("Неверный тип данных у даты")
    print(f'Курс {currency} равен {kurs} на {date_value}')