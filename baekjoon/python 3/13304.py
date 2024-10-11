# 문제 링크: https://www.acmicpc.net/problem/13304

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
c = [0] * 5
for _ in range(N):
    S, Y = map(int, input().split())
    c[(S + 1) * (Y > 2) + 2 * (Y > 4)] += 1

print(-sum(map(lambda x: -x // K, c)))
