# 문제 링크: https://www.acmicpc.net/problem/4740

import sys

for input in sys.stdin:
    input = input[:-1]
    if input == '***':
        break

    print(input[::-1])
