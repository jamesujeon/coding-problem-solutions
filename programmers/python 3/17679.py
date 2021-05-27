# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    board = [[board[i][j] for i in range(m - 1, -1, -1)] for j in range(n)]

    def validate(i, j):
        return all([
            board[i][j] != '0',
            board[i][j] == board[i + 1][j],
            board[i][j] == board[i][j + 1],
            board[i][j] == board[i + 1][j + 1]
        ])

    while True:
        targets = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if validate(i, j):
                    targets.update([
                        (i, j), 
                        (i, j + 1), 
                        (i + 1, j), 
                        (i + 1, j + 1)
                    ])

        if targets:
            for target in targets:
                board[target[0]][target[1]] = '0'

            for i in range(n):
                board[i] = [block for block in board[i] if block != '0']
                board[i] += '0' * (m - len(board[i]))
        else:
            break

    return sum(col.count('0') for col in board)