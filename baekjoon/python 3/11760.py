# 문제 링크: https://www.acmicpc.net/problem/11760

n, c, g = input().split()
r, p = 0, list(c)
for i in range(int(n)):
    if c[i] == g[i]:
        r += 1
    if g[i] in p:
        p.remove(g[i])

print(r, int(n) - len(p) - r)
