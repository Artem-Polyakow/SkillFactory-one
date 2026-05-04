
"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_predict(number: int = 1) -> int:
    """Угадываем число бинарным поиском.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    left = 1
    right = 100

    while left <= right:
        count += 1

        predict_number = (left + right) // 2

        if predict_number == number:
            break

        if predict_number < number:
            left = predict_number + 1
        else:
            right = predict_number - 1

    return count


def score_game(predict_func) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает алгоритм.

    Args:
        predict_func: функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    score_game(binary_predict)