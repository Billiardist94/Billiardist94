import calendar
day = int(input('Введите день: '))
month = int(input('Введите месяц: '))
year = int(input('Введите год: '))
try:
    c = calendar.weekday(year, month, day)
except:
    ValueError
    if month == 2 or month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
        print('В этом месяце 30 дней')
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day > 31:
        print('В этом месяце 31 день')

else:
    week = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    for i in week:
        if i == c:
            print(week[i])


