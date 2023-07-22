# 문제 링크: https://www.acmicpc.net/problem/25815

y, m = map(int, input().split())

if y < 1:
    m *= 15
    y, m = m // 12, m % 12
elif y < 2:
    m *= 9
    y, m = 15 + m // 12, m % 12
else:
    m *= 4
    y, m = 24 + max(y - 2, 0) * 4 + m // 12, m % 12

print(y, m)
