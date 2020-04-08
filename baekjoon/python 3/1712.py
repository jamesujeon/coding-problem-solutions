# 문제 링크: https://www.acmicpc.net/problem/1712

a, b, c = map(int, input().split())
print(a // (c - b) + 1 if b < c else -1)