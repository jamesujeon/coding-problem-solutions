# 문제 링크: https://www.acmicpc.net/problem/4107

import sys
input = sys.stdin.readline

while True:
    N, M, K = map(int, input().split())
    if N == M == K == 0:
        break

    P = list(map(int, input().split()))
    count = N
    for i in range(1, M):
        N += P[(i - 1) % len(P)]
        count += N

    print(count)
