# 문제 링크: https://www.acmicpc.net/problem/11365

import sys

for input in sys.stdin:
    if input == 'END\n':
        break

    print(input.strip()[::-1])
