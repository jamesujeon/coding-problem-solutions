# 문제 링크: https://www.acmicpc.net/problem/1773

N, C = map(int, input().split())

t = [0] * C
for _ in range(N):
    T = int(input())
    if T == 1:
        print(C)
        quit()
    t[T - 1::T] = [1] * (C // T)

print(t.count(1))
