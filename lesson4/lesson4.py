# string formatting
# f-string
# print(f'{}')
# str.format()
# print('dasdasda {}'.format(a))


name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
message = ''
text = ''
error = ''
a = False
b = False

if age <= 0:
    text = "Ошибка: недопустимый возраст."
    a = True
elif 1 < age < 14:
    text = "Ошибка: минимальный возраст - 14 лет."
    a = True

if not name:
    if a:
        error = "Ошибка: пустое имя. и "
    else:
        error = "Ошибка: пустое имя."
        b = True
elif name.__len__() < 3:
    if a:
        error = "Ошибка: в имени должно быть минимум 3 символа. и  "
    else:
        error = "Ошибка: в имени должно быть минимум 3 символа."
        b = True

if not a and not b:
    if 16 <= age <= 17:
        message = f"Здраствуйте, {name}!\nВам {age} лет. Не забудьте получить свой первый паспорт!"
    elif 25 <= age <= 26:
        message = f"Здраствуйте, {name}!\nВам {age} лет. Вам необходимо заменить паспорт!"
    elif 45 <= age <= 46:
        message = f"Здраствуйте, {name}!\nВам {age} лет. Вам необходимо заменить паспорт во второй раз!"
    else:
        message = f"Здраствуйте, {name}!\nВам {age} лет."

print(error + text + message)
