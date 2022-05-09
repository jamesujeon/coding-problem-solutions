# 문제 링크: https://www.acmicpc.net/problem/13136

r, c, n = map(int, input().split())

print(((r + n - 1) // n) * ((c + n - 1) // n))
