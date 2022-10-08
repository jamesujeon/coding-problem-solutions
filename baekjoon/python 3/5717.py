# 문제 링크: https://www.acmicpc.net/problem/5717

import sys

for input in sys.stdin:
    M, F = map(int, input.split())
    if M == 0 and F == 0:
        break

    print(M + F)
