# 문제 링크: https://www.acmicpc.net/problem/5576

f = lambda: sum(sorted([int(input()) for _ in range(10)])[-3:])
print(f(), f())