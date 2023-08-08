# 문제 링크: https://www.acmicpc.net/problem/25869

w, h, d = map(int, input().split())

print(max(w - d * 2, 0) * max(h - d * 2, 0))
