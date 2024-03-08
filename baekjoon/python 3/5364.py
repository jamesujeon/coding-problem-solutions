# 문제 링크: https://www.acmicpc.net/problem/5364

n = int(input())
x1, y1 = map(int, input().split())
x2 = y2 = min_d = 0
for _ in range(n - 1):
    x3, y3 = map(int, input().split())
    d = ((x1 - x3)**2 + (y1 - y3)**2)**.5
    if not min_d or d < min_d:
        x2, y2 = x3, y3
        min_d = d

print(f'{x1} {y1}\n{x2} {y2}\n{min_d:.2f}')
