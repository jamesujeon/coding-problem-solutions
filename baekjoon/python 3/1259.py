# 문제 링크: https://www.acmicpc.net/problem/1259

import sys

for input in sys.stdin:
    num = int(input)
    if num == 0:
        break

    print('yes' if str(num) == str(num)[::-1] else 'no')