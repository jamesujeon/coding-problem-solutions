# 문제 링크: https://www.acmicpc.net/problem/14470

a, b, c, d, e = (int(input()) for _ in range(5))

t = 0
if a < 0:
    t += -a * c
    a = 0
if a == 0:
    t += d
t += (b - a) * e

print(t)
