# 문제 링크: https://www.acmicpc.net/problem/6877

import sys
input = sys.stdin.readline

c, r = map(int, input().split())
x = y = 0

while (s := input().strip()) != "0 0":
    a, b = map(int, s.split())
    x, y = min(max(x + a, 0), c), min(max(y + b, 0), r)

    print(x, y)
