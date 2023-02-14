board = [['-']*3 for i in range(3)]

def print_board():
    print('  0 1 2')
    for i in range(len(board)):
        print(str(i), *board[i])

def enter_number(n):
    while True:
        coord = input('введите координаты через пробел: ').split()
        if len(coord) != 2:
            print('введите 2 координаты')
            continue
        if not (coord[0].isdigit() and coord[1].isdigit()):
            print('введите числа')
            continue
        coord1 = list(map(int, coord))
        a = coord1[0]
        b = coord1[1]
        if not (0 <= a < 3 and 0 <= b < 3):
            print('координаты от 0 до 3')
            continue
        if n [a][b] != '-':
            print('клетка занята')
            continue
        break
    return a, b

def win(f, player):
    for i in range(3):
        if f[i][0] == f[i][1] == f[i][2] == player or \
                f[0][1] == f[1][i] == f[2][i] == player or \
                f[0][0] == f[1][1] == f[2][2] == player or \
                f[0][2] == f[1][1] == [2][0] == player:
            return True


count = 1
while True:
    print_board()
    if count == 10:

        print('ничья')
        break
    if count % 2 != 0:
        player = 'x'
    else:
        player = '0'

    x, y = enter_number(board)
    board [x][y] = player
    if win(board, player):
        print_board()
        print('ты выиграл')
        break
    count += 1

# я смотрела разбор проекта и потом выполняла задание, сама бы никогда в жизни не справилась :)





