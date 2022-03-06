import sys
from utils import currency_rates_adv

if __name__ == '__main__':
    # если нет параметров командной строки или их больше одного - то выводим usage
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <currency>')
        exit(1)

    currency = sys.argv[1]
    # получаем курс и дату
    value, date = currency_rates_adv(currency)
    # если такая валюта не найдена - напишем об этом
    if value is None:
        print(f'Валюта {currency} не найдена')
        exit(1)

    # выводим курс и дату
    print(f'Курс ЦБ {currency} к рублю равен {value} на {date}')


# примеры выполнения:

# makutu@MacBook-Pro-Ulia Bryukhovskikh_Yuliya_dz_4 % python3 task_4_5.py USD
# Курс ЦБ USD к рублю равен 75.7619 на 2022-02-20
# makutu@MacBook-Pro-Ulia Bryukhovskikh_Yuliya_dz_4 % python3 task_4_5.py BER
# Валюта BER не найдена
# makutu@MacBook-Pro-Ulia Bryukhovskikh_Yuliya_dz_4 % python3 task_4_5.py EUR
# Курс ЦБ EUR к рублю равен 86.1489 на 2022-02-20
# makutu@MacBook-Pro-Ulia Bryukhovskikh_Yuliya_dz_4 % python3 task_4_5.py CAD
# Курс ЦБ CAD к рублю равен 59.768 на 2022-02-20
# makutu@MacBook-Pro-Ulia Bryukhovskikh_Yuliya_dz_4 % python3 task_4_5.py BGR
# Валюта BGR не найдена