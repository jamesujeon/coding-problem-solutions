# 문제 링크: https://www.acmicpc.net/problem/1284

import sys

for input in sys.stdin:
    N = input.strip()
    if N == '0':
        break

    print(len(N) * 4 + N.count('0') - N.count('1') + 1)
