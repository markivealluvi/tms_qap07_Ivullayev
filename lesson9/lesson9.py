from time import time

numbers = list(range(1, 10))

print(
    f"Лямбда-функция, определяющая чётное число или нет: "
    f"{list(map(lambda x: x % 2 == 0 and 'Чётное' or 'Нечётное', numbers))}"
)

print(f"Переведенные в строку числа: {list(map(lambda x: str(x), numbers))}")

words = ['казак',
         'булава',
         'ручка',
         'довод',
         'пустыня',
         'мадам',
         'кабак',
         ]

print(
    f"Отфильтрованный кортеж из палиндромов: ",
    f"{list(filter(lambda word: word == ''.join(reversed(word)), words))}",
)


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        print(func(*args, **kwargs))
        end_time = time()
        total_time = end_time - start_time

        print(f"Функция {func.__name__} выполнялась {total_time}")

    return wrapper


@decorator
def str_to_digit(string: str):

    if string.isdigit():
        return f"Вы ввели положительное целое число: {int(string)}"

    elif string[0] == "-" and "." in string:
        return f"Вы ввели отрицательное дробное число: {float(string)}"

    elif string[0] == "-" and string[1 | len(string) - 2].isdigit():
        return f"Вы ввели отрицательное целое число: {int(string)}"

    elif "." in string:
        return f"Вы ввели дробное число: {float(string)}"

    else:
        return f"Вы ввели некорректное число: {string}"


number = input("Введите число!\n")
str_to_digit(number)
