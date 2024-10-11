import os
import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    try:
        with open(name, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line.strip())
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e}")


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filenames = [os.path.join(current_dir, f'file {number}.txt') for number in range(1, 5)]

    # Проверка наличия файлов
    for filename in filenames:
        print(f"Проверка наличия файла: {filename}")
        read_info(filename)

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейный вызов: {end_time - start_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов: {end_time - start_time:.6f} секунд")