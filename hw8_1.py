import numpy as np


def random_predict(number: int = 1) -> int:
    """
    Угадывает число случайным образом без использования подсказок.
    
    Args:
        number (int): Загаданное число (от 1 до 100).
        
    Returns:
        int: Количество попыток.
    """
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)
        if predict == number:
            break
    return count


def game_core_v2(number: int = 1) -> int:
    """
    Угадывает число, последовательно приближаясь к нему ±1.
    
    Args:
        number (int): Загаданное число (от 1 до 100).
        
    Returns:
        int: Количество попыток.
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while predict != number:
        count += 1
        if predict < number:
            predict += 1
        else:
            predict -= 1
    return count


def game_core_v3(number: int = 1) -> int:
    """
    Угадывает число методом бинарного поиска (деление отрезка пополам).
    
    Args:
        number (int): Загаданное число (от 1 до 100).
        
    Returns:
        int: Количество попыток.
    """
    low, high = 1, 100
    count = 0
    
    while True:
        count += 1
        predict = (low + high) // 2
        
        if predict == number:
            return count
        elif predict < number:
            low = predict + 1
        else:
            high = predict - 1


def score_game(guess_function) -> int:
    """
    Оценивает среднее количество попыток для угадывания 10 000 случайных чисел.
    
    Args:
        guess_function (callable): Функция для угадывания числа.
        
    Returns:
        int: Среднее количество попыток.
    """
    np.random.seed(42)  # для воспроизводимости результата
    numbers = np.random.randint(1, 101, size=10000)
    scores = [guess_function(n) for n in numbers]
    average_score = int(np.mean(scores))
    print(f"Алгоритм угадывает число в среднем за {average_score} попыток")
    return average_score
