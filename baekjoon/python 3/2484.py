# 문제 링크: https://www.acmicpc.net/problem/2484

import sys
input = sys.stdin.readline

max_m = 0
for _ in range(int(input())):
    a, b, c, d = sorted(map(int, input().split()))

    m = 0
    if a == d:
        m = 50000 + 5000 * a
    elif a == c or b == d:
        m = 10000 + 1000 * b
    elif a == b and c == d:
        m = 2000 + 500 * (a + c)
    elif a == b or b == c or c == d:
        m = 1000 + 100 * (a if a == b else c)
    else:
        m = 100 * max(a, b, c, d)

    max_m = max(m, max_m)

print(max_m)
