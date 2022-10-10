# 문제 링크: https://www.acmicpc.net/problem/6378

import sys

def f(N):
    if N < 10:
        return N
    return f(sum(map(int, str(N))))

for input in sys.stdin:
    N = int(input)
    if N == 0:
        break

    print(f(N))
