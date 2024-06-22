def initboard():
    # 创建一个10x10的棋盘，用字母表示棋子
    chessboardFirst = [
        [' ', 'A', ' ', 'A', ' ', 'A', ' ', 'A', ' ', 'A'],
        ['A', ' ', 'A', ' ', 'A', ' ', 'A', ' ', 'A', ' '],
        [' ', 'A', ' ', 'A', ' ', 'A', ' ', 'A', ' ', 'A'],
        ['A', ' ', 'A', ' ', 'A', ' ', 'A', ' ', 'A', ' '],
        [' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*'],
        ['*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' '],
        [' ', 'Q', ' ', 'Q', ' ', 'Q', ' ', 'Q', ' ', 'Q'],
        ['Q', ' ', 'Q', ' ', 'Q', ' ', 'Q', ' ', 'Q', ' '],
        [' ', 'Q', ' ', 'Q', ' ', 'Q', ' ', 'Q', ' ', 'Q'],
        ['Q', ' ', 'Q', ' ', 'Q', ' ', 'Q', ' ', 'Q', ' ']
    ]
    chessboardNum = chessboardFirst
    # 创建一个10x10的棋盘，用数字表示位置
    # chessboard = [[i * 10 + j if (i + j) % 2 == 0 else ' ' for j in range(10)] for i in range(10)]
    # 替换棋盘中的 A、Q 和 * 为自增数字
    count = 1
    for i in range(10):
        for j in range(10):
            if chessboard[i][j] == 'A':
                chessboardNum[i][j] = count
                count += 1
            elif chessboard[i][j] == 'Q':
                chessboardNum[i][j] = count
                count += 1
            elif chessboard[i][j] == '*':
                chessboardNum[i][j] = count
                count += 1

    # 打印替换后的棋盘
    # for row in chessboard:
    #     print(' '.join(f'{x:2d}' if isinstance(x, int) else '  ' for x in row))
    # print("\n")

    # # 打印棋盘

    # for row in chessboardFirst:
    #     print('  '.join(row))
def BoardStatus():
    sboard=chessboardFirst

    for row in sboard:
        print('  '.join(row))
    print("\n")
    for row in chessboard:
        print(' '.join(f'{x:2d}' if isinstance(x, int) else '  ' for x in row))

BoardStatus()
