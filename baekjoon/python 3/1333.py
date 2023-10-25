# 문제 링크: https://www.acmicpc.net/problem/1333

N, L, D = map(int, input().split())

N *= L + 5
t = D
while not (L <= t % (L + 5) < L + 5) and t < N:
    t += D

print(t)
