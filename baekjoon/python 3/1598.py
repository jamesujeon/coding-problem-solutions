# 문제 링크: https://www.acmicpc.net/problem/1598

a, b = map(int, input().split())

a -= 1
b -= 1
result = abs(a // 4 - b // 4) + abs(a % 4 - b % 4)

print(result)
