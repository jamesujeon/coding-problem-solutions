# 문제 링크: https://www.acmicpc.net/problem/14409

n, x = int(input()), int(input())
v = 0
for _ in range(n):
    p1, p2 = sorted(map(int, input().split()))
    v += p2 if p2 - p1 <= x else int(input())

print(v)
