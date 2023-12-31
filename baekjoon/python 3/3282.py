# 문제 링크: https://www.acmicpc.net/problem/3282

N, G = map(int, input().split())

r = [0] * N
for _ in range(G):
    g = int(input())
    while g > 0:
        if 0 in r:
            r[r.index(0)] += min(g, 2)
            g -= min(g, 2)
        else:
            r[r.index(1)] += 1
            g -= 1

for i in r:
    print(i)
