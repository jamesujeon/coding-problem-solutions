# 문제 링크: https://www.acmicpc.net/problem/2965

A, B, C = map(int, input().split())

print(max(B - A, C - B) - 1)
