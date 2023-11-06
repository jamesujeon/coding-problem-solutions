# 문제 링크: https://www.acmicpc.net/problem/1568

N = int(input())

t = 0
while N > 0:
    K = int((N * 2)**.5)
    if N < K * (K + 1) // 2:
        K -= 1
    t += K
    N -= K * (K + 1) // 2

print(t)
