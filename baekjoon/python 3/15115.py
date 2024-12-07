# 문제 링크: https://www.acmicpc.net/problem/15115

k, p, x = map(int, input().split())
f = lambda m: x * m + k * p / m

print(f"{f(round((k * p / x)**.5)):.3f}")
