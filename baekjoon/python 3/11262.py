# 문제 링크: https://www.acmicpc.net/problem/11262

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, *p = list(map(int, input().split()))

    a = int(sum(p) / n * 1000 + 0.5) / 1000
    p = int(sum(i > a for i in p) / n * 100000 + 0.5) / 1000

    print(f"{a:.3f}", f"{p:.3f}%")
