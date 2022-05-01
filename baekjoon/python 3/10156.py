# 문제 링크: https://www.acmicpc.net/problem/10156

k, n, m = map(int, input().split())

print(k * n - m if k * n > m else 0)
