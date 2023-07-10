"""
Завдання 2 – Рослини проти Зомбі

Створіть функцію, яка прийматиме два масиву несортованих чисел (перший - масив рослин, що захищається,
другий - атакуючий масив зомбі) і поверне boolean значення в залежність від того чи перемогли захисники.

➡️ Умови:

Кожен елемент масиву атакує елемент іншого масиву з тим самим індексом масиву. Той, хто вижив, - це число з найбільшим значенням.
Якщо значення однакове, вони обидва гинуть.
Якщо одне із значень відсутнє (різна довжина масивів), солдат з непустим значенням виживає.
Щоб вижити, сторона, що обороняється, повинна мати більше тих, хто вижив, ніж атакуюча сторона.
У випадку, якщо з обох боків однакова кількість людей, що вижили, перемагає команда з найбільшою початковою силою атаки.
 Якщо загальна сила атаки з обох сторін однакова, поверніть True.
Початкова сила атаки є сумою всіх значень у кожному масиві.
Тести:

zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 6, 8 ] -> True
zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4 ] -> False
zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 0, 8 ] -> True
zombies=[ 2, 1, 1, 1 ] plants=[ 1, 2, 1, 1 ] -> True
"""

zombies = [1, 3, 5, 7]
plants = [2, 4, 0, 8 ]


def validate_input(func):
    """
       Decorator that validates the input arguments of the decorated function.

       :param func: The function to be decorated.
       :return: The decorated function.
       """
    def wrapper(plants, zombies):
        if not all(isinstance(x, (int, float)) for x in plants + zombies):
            raise ValueError("Both plants and zombies must contain only numbers")
        return func(plants, zombies)
    return wrapper


@validate_input
def plant_war(plants, zombies):
    """
      Compares the arrays of plants and zombies and returns the result of the battle.

      :param plants: Array of numbers representing the strength of plants.
      :param zombies: Array of numbers representing the strength of zombies.
      :return: The result of the battle. True if plants win, False otherwise.
      """
    min_len = min(len(plants), len(zombies))
    score_plants = 0
    score_zombies = 0

    for i in range(min_len):
        if plants[i] > zombies[i]:
            score_plants += 1
        elif plants[i] < zombies[i]:
            score_zombies += 1

    if len(plants) > min_len:
        score_plants += len(plants[min_len:])
    elif len(zombies) > min_len:
        score_zombies += len(zombies[min_len:])

    if score_plants > score_zombies:
        return True
    elif score_zombies > score_plants:
        return False
    elif score_zombies == score_plants and len(plants) == len(zombies):
        return True
    elif score_zombies == score_plants and len(plants) > len(zombies):
        return True
    elif score_zombies == score_plants and len(plants) < len(zombies):
        return False


print(plant_war(plants, zombies))
