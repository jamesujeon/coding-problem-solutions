# 문제 링크: https://www.acmicpc.net/problem/24083

A, B = (int(input()) for _ in range(2))

print((A + B - 1) % 12 + 1)
