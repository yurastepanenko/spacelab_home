"""🟣 Завдання 3 – Генератор розкладу

Створіть функцію, яка генерує розклад робочих днів працівника.

➡️ Умови:

Функція приймає кількість днів, на які потрібно скласти розклад, кількість днів роботи,
кількість днів відпочинку та дату початку розкладу.
Функція повертає розклад робочих днів співробітника, який генерується починаючи з start_date на days днів уперед,
 враховуючи що співробітник чергує робочі дні (work_days) та дні відпочинку (rest_days).
Функція має повернути дані у форматі List[datetime.datetime]
Тести:

days: 5, work_days: 2, rest_days: 1, start_date: datetime(2020, 1, 30) ->
[
datetime.datetime(2020, 1, 30, 0, 0),
datetime.datetime(2020, 1, 31, 0, 0),
  datetime.datetime(2020, 2, 2, 0, 0),
datetime.datetime(2020, 2, 3, 0, 0)
]"""


def get_work_shedule(days, work_days, rest_days, start_date):
    result = []
    return result


print(get_work_shedule(5, 2, 1, (2020, 1, 30)))