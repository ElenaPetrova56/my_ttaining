class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name} и погиб.")

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name} и погиб.")

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределение для съедобных фруктов


# Пример использования
# Создаем животных
mammal = Mammal("Медведь")
predator = Predator("Тигр")

# Создаем растения
flower = Flower("Роза")
fruit = Fruit("Яблоко")

# Тестируем действия
# Попробуем накормить животных съедобным фруктом
mammal.eat(fruit)    # Вывод: Медведь съел Яблоко
predator.eat(fruit)   # Вывод: Тигр съел Яблоко

