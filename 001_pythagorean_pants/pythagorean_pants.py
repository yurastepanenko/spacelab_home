"""
Завдання 1 - Піфагорові штани

Створіть функцію, яка прийматиме масив несортованих чисел і поверне boolean значення залежно від того,
 чи можна із заданих значень скласти піфагорів трикутник з відповідними довжинами сторін.

Тести:
[5, 3, 4] -> True
[6, 8, 10] -> True
[100, 3, 65] -> False
"""
test_array = [5, 3, 4]
test_array_2 = [6, 8, 10]
test_array_3 = [100, 3, 65]
test_array_4 = [100, 3, '65']


def validate_array(func):
    def wrapper(arr):
        if len(arr) != 3 or not all(isinstance(x, (int, float)) for x in arr):
            raise ValueError("The array must contain exactly 3 numbers")
        return func(arr)
    return wrapper


@validate_array
def pythagorean_pants(custom_array):
    """
    function to accept an array of unsorted numbers and turn boolean values
    How can you add up the pythagorean tricot from the given values with double-sided dozhins of the sides.
    :param custom_array: takes an array of numbers
    :return: result - boolean
    """
    leg_1, leg_2, hypotenuse = sorted(custom_array)

    if pow(leg_1, 2) + pow(leg_2, 2) == pow(hypotenuse, 2):
        return True
    else:
        return False


print(pythagorean_pants(test_array))
print(pythagorean_pants(test_array_2))
print(pythagorean_pants(test_array_3))
print(pythagorean_pants(test_array_4))
