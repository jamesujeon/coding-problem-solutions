# 문제 링크: https://www.acmicpc.net/problem/14579

a, b = map(int, input().split())

result = 1
for i in range(a, b + 1):
    result *= (i * i + i) // 2

print(result % 14579)
