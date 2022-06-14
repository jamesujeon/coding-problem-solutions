# 문제 링크: https://www.acmicpc.net/problem/14489

A, B = map(int, input().split())
C = int(input())

print(A + B - C * 2 * int(A + B >= C * 2))
