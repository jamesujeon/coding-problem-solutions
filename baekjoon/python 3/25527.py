# 문제 링크: https://www.acmicpc.net/problem/25527

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    v = list(map(int, input().split()))
    print(sum(v[i - 1] < v[i] > v[i + 1] for i in range(1, len(v) - 1)))
