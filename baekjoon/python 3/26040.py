# 문제 링크: https://www.acmicpc.net/problem/26040

A = input()
for b in input().split():
    A = A.replace(b, b.lower())

print(A)
