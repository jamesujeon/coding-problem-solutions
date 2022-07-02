# 문제 링크: https://www.acmicpc.net/problem/18414

X, L, R = map(int, input().split())

if X < L:
    print(L)
elif X > R:
    print(R)
else:
    print(X)
