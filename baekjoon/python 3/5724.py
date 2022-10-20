# 문제 링크: https://www.acmicpc.net/problem/5724

import sys

result = [0] * 101
for i in range(1, len(result)):
    result[i] = result[i - 1] + i**2

for input in sys.stdin:
    N = int(input)
    if N == 0:
        break

    print(result[N])
