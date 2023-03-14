# 문제 링크: https://www.acmicpc.net/problem/16625

p, q, s = map(int, input().split())

gcd = 1
for i in range(2, max(p, q) + 1):
    if p % i == 0 and q % i == 0:
        gcd = i

print("yes" if p * q // gcd <= s else "no")
