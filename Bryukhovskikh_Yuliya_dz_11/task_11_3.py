from pprint import pprint


class NotNumber(Exception):

    def __init__(self, text):
        self.text = text


if __name__ == '__main__':
    result = []
    while True:
        try:
            item = input('Введите число или "stop":')
            if item == 'stop':
                break
            if not item.isdigit():
                raise NotNumber('Это не число')
        except NotNumber as err:
            print(err)
        else:
            result.append(int(item))
    pprint(result)