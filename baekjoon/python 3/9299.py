# 문제 링크: https://www.acmicpc.net/problem/9299

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    n, *x = map(int, input().split())

    x = [x[j] * (n - j) for j in range(n)]
    n -= 1

    print(f"Case {i}: {n} {' '.join(map(str, x))}")
