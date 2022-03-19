# 문제 링크: https://www.acmicpc.net/problem/1964

N = int(input())

result = N + 1 + 3 * N * (N + 1) // 2

print(result % 45678)
