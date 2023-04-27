# 문제 링크: https://www.acmicpc.net/problem/21645

n, m, k = map(int, input().split())

print((min(m, k - 1) + m // k) * n)
