# 문제 링크: https://www.acmicpc.net/problem/25191

N = int(input())
A, B = map(int, input().split())

print(min(A // 2 + B, N))
