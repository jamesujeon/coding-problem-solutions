# 문제 링크: https://www.acmicpc.net/problem/24805

a, b, h = map(int, input().split())

print(max((h - b - 1) // (a - b) + 1, 1))
