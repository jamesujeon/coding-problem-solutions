# 문제 링크: https://www.acmicpc.net/problem/27225

n, m = int(input()), int(input())

print(min(n, m) * 2 + (n + m) % 2)
