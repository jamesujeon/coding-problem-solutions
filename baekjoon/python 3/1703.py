# 문제 링크: https://www.acmicpc.net/problem/1703

import sys

for input in sys.stdin:
    input = input.strip()
    if input == '0':
        break

    input = list(map(int, input.split()))[1:]
    result = 1
    for i in range(0, len(input), 2):
        result = result * input[i] - input[i + 1]

    print(result)
