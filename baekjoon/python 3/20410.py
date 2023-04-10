# 문제 링크: https://www.acmicpc.net/problem/20410

m, s, x1, x2 = map(int, input().split())

for a in range(m):
    for c in range(m):
        if (a * s + c) % m == x1 and (a * x1 + c) % m == x2:
            print(a, c)
            exit()
