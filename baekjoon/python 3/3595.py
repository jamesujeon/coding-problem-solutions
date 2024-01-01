# 문제 링크: https://www.acmicpc.net/problem/3595

n = int(input())

s = []
for a in range(1, int(n**(1/3)) + 2):
    if n % a == 0:
        for b in range(a, int((n // a)**.5) + 1):
            if (n // a) % b == 0:
                c = n // a // b
                s.append((a + b + c, a, b, c))

print(*min(s)[1:])
