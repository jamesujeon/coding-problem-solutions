# 문제 링크: https://www.acmicpc.net/problem/25175

N, M, K = map(int, input().split())

print((M + K - 4) % N + 1)
