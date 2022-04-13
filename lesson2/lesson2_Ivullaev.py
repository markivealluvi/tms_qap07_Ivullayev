# 1. Задания для самостоятельной работы
# Создать 3 переменных с одинаковыми данными с одинаковыми идентификаторами
#
# 2. Создать 2 перменных с одинаковыми данными с разными
# идентификаторами
#
# 3. Поменять их типы так, чтобы у 1х трех были разные идентификаторы,
# а у 2х последних были одинаковые

number1 = 123456
number2 = 123456
number3 = 123456
print('id(number1) =', id(number1))
print('id(number2) =', id(number2))
print('id(number3) =', id(number3))
print()

list_numbers = [str(number1), str(number2), str(number3)]
print('id(number1) =', id(list_numbers[0]))
print('id(number2) =', id(list_numbers[1]))
print('id(number3) =', id(list_numbers[2]))

print()
age1 = [22]
age2 = [22]
print('id(age1) =', id(age1))
print('id(age2) =', id(age2))
age1 = 22
age2 = 22

print()
print('id(age1) =', id(age1))
print('id(age2) =', id(age2))
