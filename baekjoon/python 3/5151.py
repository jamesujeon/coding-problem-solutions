# 문제 링크: https://www.acmicpc.net/problem/5151

import sys
input = sys.stdin.readline

for k in range(1, int(input()) + 1):
    n, m, T = map(int, input().split())

    D = [0] * n
    for _ in range(m):
        i, t, d = input().split()
        if 0 <= T - int(t) < 1000:
            D[int(i) - 1] += float(d)

    y_v = n_v = 0
    for i in range(n):
        if input().strip() == 'Y':
            y_v += 1
        else:
            n_v += 1 / (1 + (D[i] / 10000))

    print(f'Data Set {k}:\n{y_v:.2f} {n_v:.2f}\n')
