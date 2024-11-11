# 문제 링크: https://www.acmicpc.net/problem/14563

input()
for n in map(int, input().split()):
    d = sum(set(sum(([i, n // i] for i in range(1, int(n**.5) + 1) if n % i == 0), []))) - n
    print(['Deficient', 'Abundant', 'Perfect'][(d >= n) + (d == n)])
