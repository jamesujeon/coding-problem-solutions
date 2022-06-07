# 문제 링크: https://www.acmicpc.net/problem/16204

N, M, K = map(int, input().split())

print(min(M, K) + (N - max(M, K)))
