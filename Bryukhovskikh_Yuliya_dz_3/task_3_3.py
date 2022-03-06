def thesaurus(*args) -> dict:
    dict_out = {}
    # пройтись по списку args
    for name in args:
        # найти первую букву имени
        l = name[0]
        # если ключа нет, то создаём список
        if dict_out.get(l) is None:
            dict_out[l] = []
        # добавляем имя в список
        dict_out[l].append(name)
    # соритруем словарь по алфавиту
    dict_out = dict(sorted(dict_out.items(), key=lambda x: x[0]))
    # возвращаем словарь
    return dict_out


# Проверяем работу функции на тестовых данных
print(thesaurus("Иван", "Мария", "Пётрух", "Илья"))
print(thesaurus("Юлия", "Сергей", "Юлёна", "Вадим", "Андрей"))
print(thesaurus("Олька", "Ян", "Димон"))