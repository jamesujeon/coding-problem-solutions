# 문제 링크: https://www.acmicpc.net/problem/3028

c = [1, 0, 0]
for i in input():
    if i == 'A':
        c[0], c[1] = c[1], c[0]
    elif i == 'B':
        c[1], c[2] = c[2], c[1]
    elif i == 'C':
        c[0], c[2] = c[2], c[0]

print(c.index(1) + 1)
