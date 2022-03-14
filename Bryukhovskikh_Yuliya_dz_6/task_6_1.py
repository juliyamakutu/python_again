import re
from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """
    Парсит строку на атрибуты и возвращает кортеж атрибутов
    (<remote_addr>, <request_type>, <requested_resource>)
    :param line: построчно принимает файл с логоми
    :return tuple: (<remote_addr>, <request_type>, <requested_resource>)
    """
    result = re.match(r'([0-9a-f:.]+)\s+-\s+-\s+\[.+\]\s+"([A-Z]+)\s+([0-9a-zA-Z_/]+)', line)
    return result.groups() if result else None


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

pprint(list_out)
