# 문제 링크: https://www.acmicpc.net/problem/15128

p1, q1, p2, q2 = map(int, input().split())

print(int((p1 * p2) % (q1 * q2 * 2) == 0))
