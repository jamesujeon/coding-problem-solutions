# 문제 링크: https://www.acmicpc.net/problem/24087

S, A, B = (int(input()) for _ in range(3))

print(250 + max(((S - A - 1) // B + 1) * 100, 0))
