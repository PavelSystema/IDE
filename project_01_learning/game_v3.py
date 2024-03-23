"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Угадываем число, сперва определяя больше ли оно чем 50 или меньше. Затем 
    используем шаг коррекции начиная с 32 (на каждой итерации уменьшая шаг в два
    раза) и в зависисмости от того больше оно или меньше прибавляем или убавляем шаг
    коррекции

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = 50
    correction = 32
    while number != predict:
        count += 1
        if predict < number:
            predict += correction

        elif predict > number:
            predict -= correction
        correction /= 2
    # Ваш код заканчивается здесь    
    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    #print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
