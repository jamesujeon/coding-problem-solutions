# 문제 링크: https://www.acmicpc.net/problem/23375

x, y = map(int, input().split())
r = int(input())

print(x - r, y + r)
print(x + r, y + r)
print(x + r, y - r)
print(x - r, y - r)
