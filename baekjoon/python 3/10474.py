# 문제 링크: https://www.acmicpc.net/problem/10474

import sys

for input in sys.stdin:
    a, b = map(int, input.split())
    if a == b == 0:
        break

    print(f"{a // b} {a % b} / {b}")
