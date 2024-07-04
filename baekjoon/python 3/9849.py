# 문제 링크: https://www.acmicpc.net/problem/9849

import sys
input = sys.stdin.readline

i1 = j1 = 0
i2 = j2 = 10000
for _ in range(int(input())):
    x1, x2, y1, y2 = map(int, input().split())
    i1, i2, j1, j2 = max(x1, i1), min(x2, i2), max(y1, j1), min(y2, j2)

print(max(i2 - i1, 0) * max(j2 - j1, 0))
