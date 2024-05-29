# 문제 링크: https://www.acmicpc.net/problem/7770

n = int(input())

m = i = 0
while m <= n:
    m += 2 * i * (i + 1) + 1
    i += 1

print(i - 1)
