# 문제 링크: https://www.acmicpc.net/problem/1297

d, h, w = map(int, input().split())

ratio = (d**2 / (h**2 + w**2))**.5
h, w = int(h * ratio), int(w * ratio)

print(h, w)
