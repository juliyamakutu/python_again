def convert_time(duration: int) -> str:
    # вычисляем секунды, часы, минуты и секунды
    s = duration % 60
    m = duration // 60 % 60
    h = duration // 60 // 60 % 60
    d = duration // 60 // 60 // 60 % 24

    if d > 0:
        # если дней больше, чем ноль, то результат записываем так
        result = f'{d} дн, {h} час, {m} мин, {s} сек'
    elif d == 0 and h > 0:
        result = f'{h} час, {m} мин, {s} сек'
    elif h == 0 and m > 0:
        result = f'{m} мин, {s} сек'
    else:
        result = f'{s} сек'

    return result


duration = 80542
result = convert_time(duration)
print(result)




