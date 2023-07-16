# 문제 링크: https://www.acmicpc.net/problem/25774

d1, m1, y1, n = map(int, input().split())
d2, m2, y2 = map(int, input().split())

print(((d2 + m2 * 30 + y2 * 360) - (d1 + m1 * 30 + y1 * 360) + n - 1) % 7 + 1)
