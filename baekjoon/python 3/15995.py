# 문제 링크: https://www.acmicpc.net/problem/15995

a, m = map(int, input().split())

x = 1
while a * x % m != 1:
    x += 1

print(x)
