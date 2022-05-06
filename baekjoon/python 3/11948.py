# 문제 링크: https://www.acmicpc.net/problem/11948

a, b, c, d, e, f = (int(input()) for _ in range(6))

print(sum(sorted([a, b, c, d])[1:]) + max(e, f))
