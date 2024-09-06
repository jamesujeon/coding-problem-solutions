# 문제 링크: https://www.acmicpc.net/problem/11213

n = int(input())
a = list(map(int, input().split()))

c = [0] * 6
for i in range(n):
    c[a[i] - 1] += 1

m = 0
for i in range(6):
    if c[i] == 1:
        m = i + 1

print(a.index(m) + 1 if m else 'none')
