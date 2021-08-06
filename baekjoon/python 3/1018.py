# 문제 링크: https://www.acmicpc.net/problem/1018

import sys
from itertools import accumulate
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]


accus = [[0] * (m + 1)]
for i in range(1, n + 1):
    accus.append([0] + list(accumulate((i + j + (s == 'B')) % 2 for j, s in enumerate(board[i - 1]))))
    for j in range(1, m + 1):
        accus[i][j] += accus[i - 1][j]

min_count = 32
for i in range(8, n + 1):
    for j in range(8, m + 1):
        count = accus[i][j] - accus[i - 8][j] - accus[i][j - 8] + accus[i - 8][j - 8]
        min_count = min(count, 64 - count, min_count)


print(min_count)