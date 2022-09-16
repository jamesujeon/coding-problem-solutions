# 문제 링크: https://www.acmicpc.net/problem/2975

import sys

for input in sys.stdin:
    input = input.strip()
    if input == '0 W 0':
        break

    input = input.split()
    result = int(input[0]) + int(input[2]) * (-1 if input[1] == 'W' else 1)
    print(result if result >= -200 else 'Not allowed')
