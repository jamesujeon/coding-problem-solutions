# 문제 링크: https://www.acmicpc.net/problem/3040

n = [int(input()) for _ in range(9)]

m = sum(n) - 100
for i in sorted(n, reverse=True):
    if m - i in n:
        n.remove(i)
        n.remove(m - i)
        break

for i in n:
    print(i)
