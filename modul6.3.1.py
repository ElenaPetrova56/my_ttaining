class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def run(self, dx):
        super().run(dx)  # Вызываем метод run() из класса Horse

    def fly(self, dy):
        super().fly(dy)  # Вызываем метод fly() из класса Eagle

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


# Создаем объект Pegasus
pegasus = Pegasus()

print("Первоначальное положение:", pegasus.get_pos())

pegasus.move(5, 10)
print("Положение после движения:", pegasus.get_pos())

print("Звук пегаса:", end=' ')
pegasus.voice()

pegasus.move(3, 4)
print("Положение после нового движения:", pegasus.get_pos())



