# 문제 링크: https://www.acmicpc.net/problem/9784

for t in range(1, int(input()) + 1):
    n, P, Q = map(int, input().split())
    w = sorted(map(int, input().split()))

    i = g = 0
    while i < n and g <= Q:
        g += w[i]
        i += 1

    print(f"Case {t}: {min(i - 1 + (g <= Q), P)}")
