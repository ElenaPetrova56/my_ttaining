import time
from threading import Thread


class Knight(Thread):
    total_enemies = 100  # Общее количество врагов

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while Knight.total_enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день)
            self.days += 1

            # Сражение
            if Knight.total_enemies > 0:
                # Уменьшаем количество врагов на силу рыцаря
                Knight.total_enemies -= self.power

                # Уровень врагов не должен быть меньше 0
                if Knight.total_enemies < 0:
                    Knight.total_enemies = 0

                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {Knight.total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидаем завершения всех потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")
