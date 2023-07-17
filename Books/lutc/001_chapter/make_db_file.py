# bob = ['Bob Smith', 42, 30000, 'software']
# sue = ['Sue Jones', 45, 40000, 'hardware']
# print(bob[0], sue[2])
# print(bob[0].split()[-1] )


# bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
# sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
# print(bob)
#
#
# names = ['name', 'age', 'pay', 'job']
# values = ['Sue Jones', 45, 40000, 'hdw']
# print(list(zip(names, values)))


dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'
def storeDbase(db, dbfilename=dbfilename):
    "сохраняет базу данных в файл"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def loadDbase(dbfilename=dbfilename):
    "восстанавливает данные, реконструируя базу данных"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)