# 문제 링크: https://www.acmicpc.net/problem/9897

L, G, R = map(int, input().split())

g = {}
for _ in range(G):
    n, a, d = input().split()
    g[n] = {i for i in range(int(a), L + 1, int(d))}

l = set()
for _ in range(R):
    l ^= g[input()]

print(len(l))
