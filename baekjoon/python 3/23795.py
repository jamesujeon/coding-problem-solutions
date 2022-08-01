# 문제 링크: https://www.acmicpc.net/problem/23795

import sys

total = 0
for input in sys.stdin:
    input = input.strip()
    if input == '-1':
        break

    total += int(input)

print(total)
