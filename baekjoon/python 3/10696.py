# 문제 링크: https://www.acmicpc.net/problem/10696

for T in range(1, int(input()) + 1):
    N, X = input().split()
    X = int(X)

    R = 0
    for d in N:
        R = (R * 10 + int(d)) % X

    print(f"Case {T}: {R}")
