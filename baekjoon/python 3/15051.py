# 문제 링크: https://www.acmicpc.net/problem/15051

a1, a2, a3 = (int(input()) for _ in range(3))

print(min(a1 * 2 + a2, a1 + a3, a2 + a3 * 2) * 2)
