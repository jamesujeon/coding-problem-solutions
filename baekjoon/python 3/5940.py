# 문제 링크: https://www.acmicpc.net/problem/5940

A, B = map(int, input().split())

E = 0
for i in range(A + 1, 63):
    if int(str(2 ** i)[0]) == B:
        E = i
        break

print(E)
