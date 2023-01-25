# 문제 링크: https://www.acmicpc.net/problem/5341

import sys

for input in sys.stdin:
    n = int(input)
    if n == 0:
        break

    print(n * (n + 1) // 2)
