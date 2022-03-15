# 문제 링크: https://www.acmicpc.net/problem/1100

board = [input() for _ in range(8)]

result = sum(f == 'F' for i in range(len(board)) for f in board[i][i % 2::2])

print(result)
