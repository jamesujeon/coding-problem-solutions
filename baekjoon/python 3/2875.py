# 문제 링크: https://www.acmicpc.net/problem/2875

N, M, K = map(int, input().split())

print(min(N // 2, M, (N + M - K) // 3))
