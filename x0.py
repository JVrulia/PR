board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
    ]
print(board)
print('  0 1 2')
for i in range(len(board)):
    print(str(i), *board[i])

def show_b(f):
    print('  0 1 2')
    for i in range(len(f)):
        print(str(i) + ' ' + ' '.join(f[i]))
show_b(board)

axe_x = '  a  b  c d'
print(axe_x)
for row, i in zip(board, axe_x.split()):
    print(f" {i} {' '.join(str(j) for j in row)}")







