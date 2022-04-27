# 문제 링크: https://www.acmicpc.net/problem/8674

a, b = map(int, input().split())

print(min(a, b) if a * b % 2 else 0)
