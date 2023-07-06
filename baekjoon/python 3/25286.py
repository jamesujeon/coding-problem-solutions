# 문제 링크: https://www.acmicpc.net/problem/25286

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    y, m = map(int, input().split())

    m -= 1
    if m == 0:
        y -= 1
        m = 12

    d = 31 if m in (1, 3, 5, 7, 8, 10, 12) else 30
    if m == 2:
        d = 28 + int((y % 4 == 0 and y % 100 > 0) or y % 400 == 0)

    print(y, m, d)
