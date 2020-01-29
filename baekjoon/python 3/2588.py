# 문제 링크: https://www.acmicpc.net/problem/2588

a, b = int(input()), int(input())

print(a * (b % 10))
print(a * ((b // 10) % 10))
print(a * ((b // 100) % 10))
print(a * b)