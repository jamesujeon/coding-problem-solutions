# 문제 링크: https://www.acmicpc.net/problem/16673

C, K, P = map(int, input().split())

print(sum(K * n + P * n**2 for n in range(1, C + 1)))
