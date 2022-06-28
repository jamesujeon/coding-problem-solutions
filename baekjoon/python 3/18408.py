# 문제 링크: https://www.acmicpc.net/problem/18408

A, B, C = map(int, input().split())

print(B if A == B or B == C else C)
