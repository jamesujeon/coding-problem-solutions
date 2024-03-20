# 문제 링크: https://www.acmicpc.net/problem/5618

from math import gcd

_, n = input(), list(map(int, input().split()))
g = gcd(n[0], n[1], n[-1])
s = set(sum(([i, g // i] for i in range(1, int(g**.5) + 1) if g % i == 0), []))

for i in sorted(s):
    print(i)
