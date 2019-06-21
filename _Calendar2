import calendar

def search(year, month, day1):
    while year >= 2019 and 1 <= month <= 12 and day1 == 1:
        yield year, month, day1
        month -= 1
        if not month:
            year -= 1

latest_year, latest_month, day2 = 2019, 6, 1
your_day = input('Введите день: ')
day = {'Monday': 0,
       'Tuesday': 1,
       'Wednesday': 2,
       'Thursday': 3,
       'Friday': 4,
       'Saturday': 5,
       'Sunday': 6}

for i in search(latest_year, latest_month, day2):
    if calendar.weekday(*i) == day[your_day]:
        print(*i)
        break
