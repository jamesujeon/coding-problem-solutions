# 문제 링크: https://www.acmicpc.net/problem/2530

a, b, c = map(int, input().split())
d = int(input())

s = a * 3600 + b * 60 + c + d
h, m, s = (s // 3600) % 24, (s // 60) % 60, s % 60

print(h, m, s)
