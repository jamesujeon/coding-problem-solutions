# 문제 링크: https://www.acmicpc.net/problem/4766

import sys

prev = float(input())
for input in sys.stdin:
    input = float(input)
    if input == 999:
        break

    print(f'{input - prev:.2f}')

    prev = input
