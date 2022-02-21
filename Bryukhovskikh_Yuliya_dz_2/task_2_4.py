def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    for employee in list_in:
        # делим строку по словам, берём последнее слово и приводим к корректному виду
        list_out.append(f"Привет, {employee.split()[-1].capitalize()}!")

    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)