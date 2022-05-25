# 1. Сохранить данные о машине в файл в json формате.
# 2. Доделать классы машин, сделав их датаклассом. Сделать возможность сравнения по году выпуска машин.
# 3. Загрузить машины из json файла.
# 4. Написать функцию, которая создает несколько машин и сохраняет их в файл, если файла нет или он пустой.
import json
from dataclasses import asdict

from models import Car

car1 = Car(label="Porsche", color="Black", production_date=2021, max_speed=150)
car1_info = asdict(car1)

car2 = Car(label="LADA", color="White", production_date=2017, max_speed=120)
car2_info = asdict(car2)

print(f"Сравнение по году выпуска автомобилей: car1 > car2 = {car1 > car2}")

with open("autos.json", "w") as json_file:
    json.dump(car1_info, json_file)

with open("autos.json") as json_file:
    car3 = json.load(json_file)

print(f"Загрузка машины из json-файла: {car3}")

list1 = Car.create_autos("Lincoln", "Black", 1989, 220)
