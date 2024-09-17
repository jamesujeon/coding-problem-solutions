# 문제 링크: https://www.acmicpc.net/problem/11640

import sys
input = sys.stdin.readline

for T in range(int(input())):
    R, P, D = map(int, input().split())
    i, m = [], 0
    for _ in range(R):
        n, w, p = input().split()
        if float(p) == 100:
            m = float(w) * D / P
        i.append((n, float(p) / 100))

    print(f"Recipe # {T + 1}")
    for n, p in i:
        print(f"{n} {m * p:.1f}")
    print('-' * 40)
