p = input('Enter some phrase: ')

p2 = p.upper()  # Заглавные буквы в строке

a = []  # Создаем пустой список

for i in p2:
    if i == ' ' or i == '.' or i == ',' or i == '!':  # Исключения, которые не попадут в список
        continue
    else:
        a.append(i)  # Заполняем список

if a[::1] == a[::-1]:  # Проверка на палиндром
    print(p, 'is a palindrom')
else:
    print(p, 'is not a palindrom')
