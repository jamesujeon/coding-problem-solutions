# 문제 링크: https://www.acmicpc.net/problem/28225

n, f = map(int, input().split())

t = []
for i in range(n):
    x, v = map(int, input().split())
    t.append(((f - x) / v, i + 1))

print(min(t)[1])
