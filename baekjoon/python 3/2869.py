# 문제 링크: https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())
print((v - b - 1) // (a - b) + 1)