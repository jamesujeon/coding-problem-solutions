# 문제 링크: https://www.acmicpc.net/problem/5101

import sys

for input in sys.stdin:
    a, b, c = map(int, input.split())
    if a == b == c == 0:
        break

    if (c - a) % b == 0 and (c - a) // b + 1 > 0:
        print((c - a) // b + 1)
    else:
        print('X')
