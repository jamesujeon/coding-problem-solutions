# 문제 링크: https://www.acmicpc.net/problem/8661

x, k, a = map(int, input().split())

print(int(x % (k + a) < k))
