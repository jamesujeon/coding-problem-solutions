# 문제 링크: https://www.acmicpc.net/problem/3733

import sys

for input in sys.stdin:
    N, S = map(int, input.split())

    print(S // (N + 1))
