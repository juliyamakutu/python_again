import sys


RECORD_LEN = 10
DB_FILE = 'my_cool_db.txt'


del sys.argv[0]
if not len(sys.argv):
    print('Please, give me some money!')
    exit(1)
for record in sys.argv:
    with open(DB_FILE, 'a') as db:
        if len(record) > RECORD_LEN:
            print(f'{record} to big to save! Please, split it!')
        else:
            db.write(record.zfill(RECORD_LEN))