# 문제 링크: https://www.acmicpc.net/problem/6013

import sys
input = sys.stdin.readline

c = [[i + 1] + list(map(int, input().split())) for i in range(int(input()))]
d = max(
    ((x1 - x2)**2 + (y1 - y2)**2, i1, i2)
    for i1, x1, y1 in c[:-1]
    for i2, x2, y2 in c[i1:]
)

print(d[1], d[2])
