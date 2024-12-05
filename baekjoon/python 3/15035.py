# 문제 링크: https://www.acmicpc.net/problem/15035

n, h, t = int(input()), list(map(int, input().split())), int(input())

m = (t % h[0], h[0])
for i in h[1:]:
    if t % i < m[0]:
        m = (t % i, i)

print(m[1])
