# 문제 링크: https://www.acmicpc.net/problem/17874

n, h, v = map(int, input().split())

print(max(h, n - h) * max(v, n - v) * 4)
