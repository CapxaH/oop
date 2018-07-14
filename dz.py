class TownCar:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))


class SportCar:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))


class WorkCar:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))


class PoliceCar:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = True

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))


class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))


class TownCar1(Car):
    pass


class SportCar1(Car):
    def __init__(self, name, color, speed, has_turbo=True):
        super().__init__(name, color, speed)
        self.has_turbo = has_turbo


class WorkCar1(Car):
    pass


class PoliceCar1(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


sportCar = SportCar1('Спортивная машина', 'Красная', 240)
townCar = TownCar1('Городская машина', 'Серая', 140)
workCar = WorkCar1('Рабочая машина', 'Жолтая', 90)
policeCar = PoliceCar1('Полицейская машина', 'Синяя', 210)

print(policeCar.is_police)
print(sportCar.speed)
print(workCar.color)
