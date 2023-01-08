# 문제 링크: https://www.acmicpc.net/problem/10406

W, N, P = map(int, input().split())

print(sum(W <= H <= N for H in map(int, input().split())))
