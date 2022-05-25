from dataclasses import dataclass, field
from os.path import exists, getsize


@dataclass(order=True)
class Car:
    label: str = field(compare=False)
    color: str = field(compare=False)
    production_date: int = field(compare=True)
    max_speed: int = field(compare=False)

    def __post_init__(self):
        if not isinstance(self.label or self.color, str):
            raise TypeError('label or color must be a string')

        if not isinstance(self.production_date or self.max_speed, int):
            raise TypeError('production_date or max_speed must be an integer')

    def info(self):
        """Информация об автомобиле."""
        return (
            f"Автомобиль {self.label}.\n"
            f"Цвет автомобиля - {self.color}.\n"
            f"Год выпуска автомобиля - {self.production_date}\n"
            f"Максимальная скорость - {self.max_speed} км/ч."
        )
        # return [self.label, self.color, self.production_date, self.max_speed]

    def start_engine(self):
        print(f"Двигатель автомобиля {self.label} заведен.\n")

    def drive(self):
        print(f"Автомобиль {self.label} едет с максимальной скоростью {self.max_speed} км/ч.")

    def put_on_lights(self):
        print(f"Включены фары автомобиля {self.label}.")

    def open_top(self):
        print(f"Крыша {self.label} опущена.")

    @staticmethod
    def create_autos(label: str, color: str, production_date: int, max_speed: int):
        """Функция, которая создает несколько авто и сохраняет их в файл."""
        car1 = Car(label, color, production_date, max_speed).info()
        car2 = Car(label, color, production_date, max_speed).info()
        car3 = Car(label, color, production_date, max_speed).info()
        list_of_cars = [car1, car2, car3]
        if exists("machines.txt") or getsize("machines.txt") == 0:
            i = 0
            while i < len(list_of_cars) - 1:
                with open("machines.txt", "w") as f:
                    f.write("\n".join(list_of_cars))
                i += 1
