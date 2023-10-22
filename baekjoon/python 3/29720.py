# 문제 링크: https://www.acmicpc.net/problem/29720

N, M, K = map(int, input().split())
print(max(N - M * K, 0), max(N - M * K + M - 1, 0))
