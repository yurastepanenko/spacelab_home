"""Сценарий в примере 1.12, например, повторно открывает
хранилище и последовательно извлекает хранящиеся в нем записи."""
import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()