# 문제 링크: https://www.acmicpc.net/problem/2991

A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

f = lambda p, a, b: int((p - 1) % (a + b) < a)

for p in [P, M, N]:
    print(f(p, A, B) + f(p, C, D))
