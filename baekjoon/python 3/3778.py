# 문제 링크: https://www.acmicpc.net/problem/3778

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    a, b = map(list, (input(), input()))

    for j in [*a]:
        if j in b:
            a.remove(j)
            b.remove(j)

    print(f'Case #{i}: {len(a + b)}')
