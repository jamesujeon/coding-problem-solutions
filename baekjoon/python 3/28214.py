# 문제 링크: https://www.acmicpc.net/problem/28214

N, K, P = map(int, input().split())
B = list(map(int, input().split()))

print(sum(B[i * K:(i + 1) * K].count(0) < P for i in range(N)))
