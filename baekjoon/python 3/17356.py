# 문제 링크: https://www.acmicpc.net/problem/17356

A, B = map(int, input().split())

M = (B - A) / 400
print(1 / (1 + 10**M))
