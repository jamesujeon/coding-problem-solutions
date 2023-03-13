# 문제 링크: https://www.acmicpc.net/problem/16546

N = int(input())
print(N * (N + 1) // 2 - sum(map(int, input().split())))
