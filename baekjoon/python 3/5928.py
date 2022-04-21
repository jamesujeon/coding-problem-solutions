# 문제 링크: https://www.acmicpc.net/problem/5928

d, h, m = map(int, input().split())

minutes = (d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11)

print(minutes if minutes >= 0 else -1)
