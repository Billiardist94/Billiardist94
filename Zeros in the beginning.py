n = int(input('Введите число: '))
lis = []    # Создаем пустой список
while len(lis) != n:
    lis.append(int(input('Введите число в список: ')))  # Заполняем список числами, количество чисел равно n

lis2 = []   #Пустой список для "0"

for i in lis:
    if i == 0:
        lis2.append(i)  #Все "0" из list вставляем в list2

    else:
        continue

while 0 in lis:
    lis.remove(0)   #Удаляем "0" из list

print(lis2 + lis)

