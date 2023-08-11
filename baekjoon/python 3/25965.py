# 문제 링크: https://www.acmicpc.net/problem/25965

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    KDA = [map(int, input().split()) for _ in range(int(input()))]
    k, d, a = map(int, input().split())

    print(sum(max(K * k - D * d + A * a, 0) for K, D, A in KDA))
