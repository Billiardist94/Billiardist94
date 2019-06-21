board = [['.' for j in range(3)] for i in range(3)]

def print_grid():
    for i in board:
        print(i[0], i[1], i[2])
print_grid()

def cross():
    string = int(input('строка для Х: '))
    column = int(input('столбец для Х: '))
    while string < 1 or string > 3 or column < 1 or column > 3 or board[string - 1][column - 1] != 'o' or board[string - 1][column - 1] != 'x':
        string = int(input('строка для Х: '))
        column = int(input('столбец для Х: '))
    board[string - 1][column - 1] = 'x'
    print_grid()

def zero():
    string = int(input('строка для О: '))
    column = int(input('столбец для О: '))
    while string < 1 or string > 3 or column < 1 or column > 3 or board[string - 1][column - 1] != 'o' or board[string - 1][column - 1] != 'x':
        string = int(input('строка для О: '))
        column = int(input('столбец для О: '))
    board[string - 1][column - 1] = 'o'
    print_grid()

def check_win():
    for k in board:
        if k[0] == k[1] == k[2] != '.':
            print('Win: ', k[0])
            break
    for v in range(2):
        if board[0][v] == board[1][v] == board[2][v] != '.':
            print('Win: ', board[0][v])
            break
    if board[0][0] == board[1][1] == board[2][2] != '.':
        print('Win: ', board[0][0])
    if board[0][2] == board[1][1] == board[2][0] != '.':
        print('Win: ', board[0][2])

check_win()

