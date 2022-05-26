# 문제 링크: https://www.acmicpc.net/problem/14623

b1, b2 = (input() for _ in range(2))

print(bin(int(b1, 2) * int(b2, 2))[2:])
