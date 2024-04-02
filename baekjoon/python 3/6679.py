# 문제 링크: https://www.acmicpc.net/problem/6679

def f(n, b):
    s = 0
    while n > 0:
        s += n % b
        n //= b
    return s

for i in range(2992, 10000):
    if f(i, 10) == f(i, 12) == f(i, 16):
        print(i)
