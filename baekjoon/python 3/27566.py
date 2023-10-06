# 문제 링크: https://www.acmicpc.net/problem/27566

r, f = map(int, input().split())

print(("up", "down")[round(f / r) % 2])
