# 문제 링크: https://www.acmicpc.net/problem/10804

c = list(range(1, 21))
for _ in range(10):
    a, b = map(int, input().split())
    c[a - 1:b] = c[a - 1:b][::-1]

print(*c)
