# 문제 링크: https://www.acmicpc.net/problem/27481

input()
r = [0] * 10
for e in input():
    if e == 'L':
        r[r.index(0)] = 1
    elif e == 'R':
        r[~r[::-1].index(0)] = 1
    else:
        r[int(e)] = 0

print(*r, sep='')
