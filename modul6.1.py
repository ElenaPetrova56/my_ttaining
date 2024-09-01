class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
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
        self.edible = True

mammal = Mammal("Медведь")
predator = Predator("Тигр")

flower = Flower("Роза")
fruit = Fruit("Яблоко")

mammal.eat(fruit)
predator.eat(fruit)

mammal.eat(flower)
predator.eat(flower)

print(f"{mammal.name} жив: {mammal.alive}, накормлен: {mammal.fed}")
print(f"{predator.name} жив: {predator.alive}, накормлен: {predator.fed}")

