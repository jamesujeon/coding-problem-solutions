# 문제 링크: https://www.acmicpc.net/problem/24867

k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())

f = lambda a, x, b, y: max(k - a, 0) * x + max(k - a - b, 0) * y

print(max(f(a, x, b, y), f(b, y, a, x)))
