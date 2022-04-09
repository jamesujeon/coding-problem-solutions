# 문제 링크: https://www.acmicpc.net/problem/2863

a, b = map(int, input().split())
c, d = map(int, input().split())

max_value = count = -1
for i in range(4):
    value = a / c + b / d
    if value > max_value:
        max_value = value
        count = i
    a, b, c, d = c, a, d, b

print(count)
