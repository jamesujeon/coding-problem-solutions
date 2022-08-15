# 문제 링크: https://www.acmicpc.net/problem/23971

H, W, N, M = map(int, input().split())

print((-H // (N + 1)) * (-W // (M + 1)))
