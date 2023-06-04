# 문제 링크: https://www.acmicpc.net/problem/23925

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    N, K, S = map(int, input().split())

    print(f"Case #{i}: {K + min(N + K - S * 2, N)}")
