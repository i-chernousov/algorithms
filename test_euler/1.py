"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23. Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

def func_euler() -> None:
    """
    Функция перебирает числа от 1 до 1000 и
    выделяет числа с отатком от деления - ноль
    прибавляя к объекту с суммой этих чисел
    """
    sum_number = 0

    for number in range(1, 1000):
        if number % 3 == 0.0 or number % 5 == 0.0:
            sum_number += number

    return print(sum_number) # result 233168

if __name__ == "__main__":
    func_euler()