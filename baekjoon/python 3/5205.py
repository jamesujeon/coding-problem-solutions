# 문제 링크: https://www.acmicpc.net/problem/5205

import sys
input = sys.stdin.readline

for k in range(1, int(input()) + 1):
    n = int(input())
    c = [list(map(int, input().split())) for _ in range(n)]

    p = []
    max_d = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            r1, g1, b1 = c[i]
            r2, g2, b2 = c[j]
            d = ((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)**.5
            if d == max_d:
                p.append((i + 1, j + 1))
            elif d > max_d:
                max_d = d
                p = [(i + 1, j + 1)]

    p = '\n'.join(f'{i} {j}' for i, j in p)
    print(f'Data Set {k}:\n{p}')
