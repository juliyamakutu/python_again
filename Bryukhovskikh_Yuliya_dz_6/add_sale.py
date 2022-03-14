import sys


RECORD_LEN = 10
DB_FILE = 'bakery.csv'


del sys.argv[0]
if not len(sys.argv):
    print('Пожалуйста, введите сумму продажи')
    exit(1)
for record in sys.argv:
    with open(DB_FILE, 'a') as db:
        if len(record) > RECORD_LEN:
            print(f'{record} слишком большое число, разделите его')
        else:
            db.write(record.replace(',', '.').zfill(RECORD_LEN))

