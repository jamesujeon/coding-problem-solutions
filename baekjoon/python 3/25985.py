# 문제 링크: https://www.acmicpc.net/problem/25985

x, y = map(int, input().split())

print(x / y * (100 - y) / (100 - x))
