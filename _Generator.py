def count(start, step):

    while True:
        print (start)
        start += step

count(int(input('Введите start: ')), int(input('Введите step: ')))