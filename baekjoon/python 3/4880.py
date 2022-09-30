# 문제 링크: https://www.acmicpc.net/problem/4880

import sys

for input in sys.stdin:
    a1, a2, a3 = map(int, input.split())
    if a1 == a2 == a3 == 0:
        break

    if a2 - a1 == a3 - a2:
        print(f'AP {a3 + a2 - a1}')
    else:
        print(f'GP {a3 * (a2 // a1)}')
