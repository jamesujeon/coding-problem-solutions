# 문제 링크: https://www.acmicpc.net/problem/4084

import sys

for input in sys.stdin:
    input = input.strip()
    if input == '0 0 0 0':
        break

    a, b, c, d = map(int, input.split())
    count = 0
    while not (a == b == c == d):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        count += 1

    print(count)
