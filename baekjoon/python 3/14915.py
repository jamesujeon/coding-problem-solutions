# 문제 링크: https://www.acmicpc.net/problem/14915

m, n = map(int, input().split())

s = ''
while m > 0:
    s += '0123456789ABCDEF'[m % n]
    m //= n

print(s[::-1] or 0)
