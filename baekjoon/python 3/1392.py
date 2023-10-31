# 문제 링크: https://www.acmicpc.net/problem/1392

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
B = sum([[i + 1] * int(input()) for i in range(N)], [])
for _ in range(Q):
    print(B[int(input())])
