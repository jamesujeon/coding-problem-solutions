# 문제 링크: https://www.acmicpc.net/problem/5293

m, n = map(int, input().split())

c = []
for _ in range(n):
    p = m // n + m % n
    m -= p
    c.append(p)

print(*c)
print(m)
