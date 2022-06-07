# 문제 링크: https://www.acmicpc.net/problem/1264

import sys

for input in sys.stdin:
    input = input.strip()
    if input == '#':
        break

    print(sum(ch in 'aeiou' for ch in input.lower()))
