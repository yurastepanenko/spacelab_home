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


from datetime import timedelta, datetime


def get_work_schedule(days, work_days, rest_days, start_date):
    result = []
    current_date = start_date
    counter_work = 0
    counter_rest = 0
    counter_days = 0

    while counter_days < days:

        if counter_work < work_days:
            result.append(current_date)
            counter_work += 1
            current_date += timedelta(days=1)
            counter_days += 1

        elif counter_rest < rest_days:
            current_date += timedelta(days=rest_days)
            counter_work = 0
            counter_days += rest_days

    return result

work_schedule = get_work_schedule(5, 2, 1, datetime(2020, 1, 30))
for day in work_schedule:
    print(day)