# 문제 링크: https://www.acmicpc.net/problem/15726

a, b, c = map(int, input().split())

print(int(max(a * b / c, a / b * c)))
