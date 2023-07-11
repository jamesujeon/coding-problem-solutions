# 문제 링크: https://www.acmicpc.net/problem/25642

A, B = map(int, input().split())

while A < 5 and B < 5:
    B += A
    A += B

print('y' + "jt"[B > 4])
