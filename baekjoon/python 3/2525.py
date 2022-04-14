# 문제 링크: https://www.acmicpc.net/problem/2525

a, b = map(int, input().split())
c = int(input())

m = a * 60 + b + c
h, m = (m // 60) % 24, m % 60

print(h, m)
