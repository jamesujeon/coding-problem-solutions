# 문제 링크: https://www.acmicpc.net/problem/6779

h, M = int(input()), int(input())
A = lambda t: -6 * t**4 + h * t**3 + 2 * t**2 + t

result = 'The balloon does not touch ground in the given time.'
for t in range(1, M + 1):
    if A(t) <= 0:
        result = f'The balloon first touches ground at hour: {t}'
        break

print(result)
