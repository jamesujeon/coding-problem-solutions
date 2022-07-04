# 문제 링크: https://www.acmicpc.net/problem/20215

w, h = map(int, input().split())

print(w + h - (w**2 + h**2)**.5)
