# 문제 링크: https://www.acmicpc.net/problem/13300

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
c = [0] * 12
for _ in range(N):
    S, Y = map(int, input().split())
    c[S * 6 + Y - 1] += 1

print(-sum(map(lambda x: -x // K, c)))
