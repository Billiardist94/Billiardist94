n = int(input('Введите число > 2: '))  # Вводим количество чисел в списке(>2)
lis = []  # Создаем пустой список

while len(lis) != n:
    if n > 2:
        lis.append(int(input('Введите число в список: ')))  # Заполняем список числами, количество чисел равно n

    else:
        print('Введено число <= 2')
        break

print(lis)
lis.sort()  # Сортируем список по возрастанию

while lis[-1] == lis[-2]:  # В случае повтора чисел в списке
    lis.pop(-1)
    if lis[-1] == lis[0]:  # Если список состоит из равных чисел
        print('Список содержит одинаковые значение:', lis[-1])
        break

print('Два наибольших числа в списке:', lis[-1], 'и', lis[-2])
