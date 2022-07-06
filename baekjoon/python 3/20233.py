# 문제 링크: https://www.acmicpc.net/problem/20233

a, x, b, y, T = (int(input()) for _ in range(5))

print(a + max(T - 30, 0) * 21 * x, b + max(T - 45, 0) * 21 * y)
