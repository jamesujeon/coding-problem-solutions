# 문제 링크: https://www.acmicpc.net/problem/7133

import sys
input = sys.stdin.readline

M, DM = map(int, input().split())
H, DH = map(int, input().split())

def f():
    C, B = map(int, input().split())
    return max(sum(max(M - DM * i, 0) for i in range(C)), sum(max(H - DH * i, 0) for i in range(B)))

print(sum(f() for _ in range(int(input()))))
