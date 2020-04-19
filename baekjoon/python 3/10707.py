# 문제 링크: https://www.acmicpc.net/problem/10707

a, b, c, d, p = [int(input()) for _ in range(5)]

print(min(a * p, b + max((p - c) * d, 0)))
