# 문제 링크: https://www.acmicpc.net/problem/25630

input()
s = input()

print(sum(a != b for a, b in zip(s, s[::-1])) // 2)
