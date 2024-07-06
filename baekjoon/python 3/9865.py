# 문제 링크: https://www.acmicpc.net/problem/9865

import sys
input = sys.stdin.readline

for n in range(1, int(input()) + 1):
    m = int(input())
    c = []
    while len(c) < m * 2:
        c += list(map(int, input().split()))

    s = [0, 0]
    for i in range(0, m * 2, 2):
        if abs(c[i] - c[i + 1]) > 1:
            s[c[i] < c[i + 1]] += max(c[i], c[i + 1])
        elif abs(c[i] - c[i + 1]) == 1:
            s[c[i] > c[i + 1]] += c[i] + c[i + 1] if min(c[i], c[i + 1]) != 1 else 6

    print(f"Game {n}: Tessa {s[0]} Danny {s[1]}")
