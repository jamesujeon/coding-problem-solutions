# 문제 링크: https://www.acmicpc.net/problem/9387

for _ in range(int(input())):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))

    if 2 in a:
        i = a.index(2)
        d = 1 if i < m - 1 else -1
    else:
        i = a.index(3)
        d = -1 if i > 0 else 1

    c = 0
    for _ in range(n):
        i += d
        if i == 0 or i == m - 1:
            d *= -1
        if a[i] == 0:
            c += 1

    print(c)
