# 문제 링크: https://www.acmicpc.net/problem/8658

n = int(input())

print(next(i for i in range(2, n) if n % i), n - 1)
