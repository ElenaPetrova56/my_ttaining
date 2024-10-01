class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.model = model
        self.engine_power = engine_power
        self.__color = color if color.lower() in self.__COLOR_VARIANTS else 'unknown'

    def get_model(self):
        return f"Модель: {self.model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

sedan = Sedan('Иван Иванов', 'Toyota Camry', 200, 'black')

sedan.print_info()

sedan.set_color('blue')
sedan.set_color('yellow')

sedan.print_info()