# 문제 링크: https://www.acmicpc.net/problem/14530

x, y = map(int, input().split())

d = (x > y) * 2 + abs(x - y)
i = 1 + (x > y)
while i < abs(x - y):
    d += i * 6
    i *= 4

print(d)
