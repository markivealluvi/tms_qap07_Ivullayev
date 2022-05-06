# 1. Реализовать абстрактный класс машины (придумайте какие методы у машины есть,
#    какие нужно у всех дочерних классов переопределять, а какие будут общие с готовой реализацией)
# 2. Реализовать несколько классов разных марок машин, наследуемых от базовой машины.
#    Переопределить абстрактные методы, свойства. Придумать новые методы, которые есть только в конкретных марках машин.
# 3. Реализовать класс абстрактный класс самолета. Должно быть как минимум один
#    или несколько одноименных атрибутов класса машины. Тоже самое из п.1
# 4. Реализовать несколько классов разных марок самолетов. Тоже самое из п.2
# 5. Создать несколько экземпляров каждой машины, каждого самолета,
#    вызвать различные методы у этих объектов. «Поиграться», скажем так.
#    А затем сделать коллекцию из этих объектов и через цикл пройтись по каждому из этих объектов
#    и вызвать те методы, которые есть во всех классах.

from abc import ABC, abstractmethod


class Car(ABC):
    label = ""
    max_speed = 120

    def __init__(self, color: str = "white"):
        self.color = color

    def info(self):
        print(
            f"Автомобиль {self.label}.\n"
            f"Цвет автомобиля - {self.color}.\n"
            f"Максимальная скорость - {self.max_speed} км/ч."
        )

    @abstractmethod
    def start_engine(self):
        print("Двигатель заведен.")

    @abstractmethod
    def drive(self):
        print("Автомобиль едет.")


class Toyota(Car):
    label = "Toyota"
    color = "black"
    max_speed = 180

    def start_engine(self):
        print(f"Двигатель автомобиля {self.label} заведен.\n")

    def drive(self):
        print(f"Автомобиль {self.label} едет с максимальной скоростью {self.max_speed} км/ч.")

    def put_on_lights(self):
        print(f"Включены фары автомобиля {self.label}.")


class Porsche(Car):
    label = "Porsche"
    color = "yellow"
    max_speed = 330

    def start_engine(self):
        print(f"Двигатель автомобиля {self.label} заведен.\n")

    def drive(self):
        print(f"Автомобиль {self.label} едет с максимальной скоростью {self.max_speed} км/ч.")

    def open_top(self):
        print(f"Крыша {self.label} опущена.")


class Airplane(ABC):
    label = ""
    max_speed = 800
    max_height = 9000
    flying_range = 7000

    def __init__(self, airline: str = ""):
        self.airline = airline

    def info(self):
        print(
            f"Самолет {self.label} авиакомпании {self.airline}.\n"
            f"Максимальная скорость - {self.max_speed} км/ч.\n"
            f"Максимальная высота - {self.max_height} м.\n"
            f"Дальность полета - {self.flying_range} км."
        )

    def start_engine(self):
        print("Двигатели самолета запущены.\n")

    @abstractmethod
    def fly(self):
        print(f"Самолет летит с максимальной скоростью - {self.max_speed} км/ч.")

    @abstractmethod
    def flaps_down(self):
        print("Закрылки выпущены.")


class Airbus(Airplane):
    label = "Airbus"
    max_speed = 1005
    max_height = 10000
    flying_range = 11000

    def fly(self):
        print(f"Самолет {self.label} набирает максимальную скорость равную {self.max_speed} км/ч.")

    def flaps_down(self):
        print(f"Закрылки самолета {self.label} выпущены.")

    def turbulence(self):
        print(f"Самолет попал в зону турбулентности.")


class Boeing(Airplane):
    label = "Boeing"
    max_speed = 920
    max_height = 9500
    flying_range = 18000

    def fly(self):
        print(f"Самолет {self.label} набирает максимальную скорость равную {self.max_speed} км/ч.")

    def flaps_down(self):
        print(f"Закрылки самолета {self.label} выпущены.")

    def flaps_up(self):
        print(f"Закрылки самолета {self.label} убраны.")


car1 = Porsche("Red")
car1.info()
car1.start_engine()
car1.drive()
car1.open_top()

car2 = Porsche("Purple")
car2.info()
car2.start_engine()
car2.drive()
car2.open_top()

car3 = Toyota("Brown")
car3.info()
car3.start_engine()
car3.drive()
car3.put_on_lights()

car4 = Toyota("Orange")
car4.info()
car4.start_engine()
car4.drive()
car4.put_on_lights()

plane1 = Airbus("Turkish Airlines")
plane1.info()
plane1.start_engine()
plane1.flaps_down()
plane1.fly()
plane1.turbulence()

plane2 = Airbus("Qatar Airlines")
plane2.info()
plane2.start_engine()
plane2.flaps_down()
plane2.fly()
plane2.turbulence()

plane3 = Boeing("Belavia")
plane3.info()
plane3.start_engine()
plane3.flaps_down()
plane3.fly()
plane3.flaps_up()

plane4 = Boeing("Lufthansa Airlines")
plane4.info()
plane4.start_engine()
plane4.flaps_down()
plane4.fly()
plane4.flaps_up()

print()

list1 = [car1, car2, car3, car4, plane1, plane2, plane3, plane4]
i = 0
while i <= len(list1) - 1:
    list1[i].info()
    list1[i].start_engine()
    i = i + 1
