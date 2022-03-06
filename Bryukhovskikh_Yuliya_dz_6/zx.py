import sys


RECORD_LEN = 10
DB_FILE = 'my_cool_db.txt'

start = int(sys.argv[1]) - 1 if len(sys.argv) > 1 else None
# end = int(sys.argv[2]) - 1 if len(sys.argv) > 2 else None

with open(DB_FILE) as db:
    if start:
        db.seek(int(start)*RECORD_LEN)
    record = db.read(RECORD_LEN)
    print(float(record))