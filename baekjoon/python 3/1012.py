# 문제 링크: https://www.acmicpc.net/problem/1012

import sys
input = sys.stdin.readline


def get_min_worm_count(field, m, n):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def mark(y, x):
        visits = [(y, x)]
        field[y][x] = -1
        while visits:
            y, x = visits.pop()
            for dy, dx in directions:
                if 0 <= y + dy < n and 0 <= x + dx < m and field[y + dy][x + dx] == 1:
                    visits.append((y + dy, x + dx))
                    field[y + dy][x + dx] = -1

    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                mark(i, j)
                count += 1

    return count


for _ in range(int(input())):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    print(get_min_worm_count(field, M, N))