# 문제 링크: https://www.acmicpc.net/problem/10180

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, D = map(int, input().split())

    count = 0
    for _ in range(N):
        v, f, c = map(int, input().split())
        if v * f / c >= D:
            count += 1

    print(count)
