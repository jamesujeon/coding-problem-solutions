# 문제 링크: https://www.acmicpc.net/problem/24310

A, B, C, D = map(int, input().split())

if max(A, B) < min(C, D) or max(C, D) < min(A, B):
    print(abs(A - B) + abs(C - D) + 2)
else:
    print(max(A, B, C, D) - min(A, B, C, D) + 1)
