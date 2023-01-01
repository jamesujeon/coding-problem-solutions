# 문제 링크: https://www.acmicpc.net/problem/10599

import sys

for input in sys.stdin:
    a, b, c, d = map(int, input.split())
    if a == b == c == d == 0:
        break

    print(c - b, d - a)
