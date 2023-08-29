# 문제 링크: https://www.acmicpc.net/problem/26535

from math import ceil

n = ceil(int(input())**.5)

print('x' * (n + 2))
for _ in range(n):
    print('x' + '.' * n + 'x')
print('x' * (n + 2))
