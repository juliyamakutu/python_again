import sys


RECORD_LEN = 10
DB_FILE = 'bakery.csv'

start = int(sys.argv[1]) - 1 if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else None

with open(DB_FILE) as db:
    db.seek(start * RECORD_LEN)
    while True:
        record = db.read(RECORD_LEN)
        if not record or (end is not None and db.tell() > end * RECORD_LEN):
            break
        print("{0:0.2f}".format(float(record)))