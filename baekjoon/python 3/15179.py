# 문제 링크: https://www.acmicpc.net/problem/15179

t = [input(), input()]
s = int(input())
c = input()

r = ''
p = [0, 0]
for i in range(s):
    if c[i] == 'H':
        p[i % 2] += 1
    elif c[i] == 'D':
        p[i % 2] = min(p[i % 2] + 2, 7)
    elif c[i] == 'O':
        p[(i + 1) % 2] += 1

    if p[0] == p[1]:
        r = 'All square'
    else:
        r = f"{t[p[0] < p[1]]} is winning"
    if p[0] > 6 or p[1] > 6:
        r = f"{t[p[0] < p[1]]} has won"
        break

print(f"{t[0]} {p[0]} {t[1]} {p[1]}. {r}.")
